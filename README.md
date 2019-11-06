# Pylint Starlark Plugin

This plugin allows you to run pylint on Starklark files, by doing an AST transform of load() calls into python import statements.

To use it, run `pip install pylint-starlark-plugin`, then you can call pytlint via `pylint --load-plugins pylint-starlark-plugin file.py`.
