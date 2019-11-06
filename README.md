# Pylint Starlark Plugin

This plugin allows you to run pylint on Starlark files, by doing an AST transform of load() calls into python import statements.

To use it, run `pip3 install pylint-starlark-plugin`, then you can call pytlint via `pylint --load-plugins pylint_starlark_plugin file.py`.
