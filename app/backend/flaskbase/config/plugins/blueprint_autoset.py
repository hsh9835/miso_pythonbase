import os
from importlib import import_module

routesName = 'routes'


def bpName(_path):
    bpModulePath = os.path.dirname(__file__) + '/' + routesName + '/'
    return _path.replace(bpModulePath, '').replace('.py', '')


def register_blueprints(app, directory=f"{routesName}", parent_prefix=''):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            subdirectory_prefix = f"{parent_prefix}/{entry}" if parent_prefix else entry
            register_blueprints(app, full_path, subdirectory_prefix)
        elif entry.endswith('.py') and entry != '__init__.py':
            module_name = os.path.splitext(entry)[0]
            uripath = f"{directory}/{module_name}" if parent_prefix else f"{directory}/{module_name}"
            module_path = uripath.replace("/", '.')
            module = import_module(module_path)

            app.register_blueprint(module.bp, url_prefix=f"/{uripath.replace(routesName, '')}")
