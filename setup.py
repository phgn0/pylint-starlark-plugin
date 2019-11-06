from distutils.core import setup

setup(
  name = 'pylint-starlark-plugin',         # How you named your package folder (MyLib)
  packages = ['pylint_starlark_plugin'],   # Chose the same as "name"
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Run pylint on Starklark files.',   # Give a short description about your library
  long_description='''
This plugin allows you to run pylint on Starklark files, by doing an AST transform of load() calls into python import statements.

To use it, run `pip3 install pylint-starlark-plugin`, then you can call pytlint via `pylint --load-plugins pylint-starlark-plugin file.py`.
  ''',
  long_description_content_type="text/markdown",
  author = 'Peter Hagen',                   # Type in your name
  author_email = 'peter@phgn.io',      # Type in your E-Mail
  url = 'https://github.com/phgn0/pylint-starlark-plugin',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/phgn0/pylint-starlark-plugin/archive/1.0.tar.gz',    # I explain this later on
  keywords = ['pylint', 'starlark', 'plugin'],   # Keywords that define your package best
  install_requires=[
    'jedi',
    'astroid',
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
