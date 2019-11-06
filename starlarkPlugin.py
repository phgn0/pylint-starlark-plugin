import astroid

def register(linter):
  # Needed for registering the plugin.
  pass

def transform(expr_node):
  # transform python expressions containing a load() call
  inner_node = expr_node.value
  if isinstance(inner_node, astroid.Call) and hasattr(inner_node.func, 'name') and inner_node.func.name == 'load':
    import_node = transform_import(inner_node)
    import_node.parent = expr_node.parent

    add_imported_variables(import_node, import_node.parent)
    return import_node

def transform_import(node):
  # transform load() statement into ImportFrom node
  from_name = node.args[0].value
  from_name = from_name.split('.')[0]  # remove file extension
  from_name = from_name.replace('/', '.')  # to python syntax

  imported_names = map(lambda const_node: const_node.value, node.args[1:])
  name_tuples = [(name, None) for name in imported_names]  # names are imported without alias

  return astroid.nodes.ImportFrom(
    fromname=from_name,
    names=name_tuples,
    level=None,
    lineno=node.lineno,
    col_offset=node.col_offset,
    parent=node.parent
  )

def add_imported_variables(import_node, module):
  # add imported names to local variables
  for name, _ in import_node.names:
    if name not in module.locals:
      module.locals[name] = []
    module.locals[name].append(import_node)

astroid.MANAGER.register_transform(astroid.Expr, transform)
