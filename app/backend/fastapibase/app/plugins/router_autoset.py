# app.plugins.router_autoset.py

import os
from importlib import import_module

from fastapi import APIRouter

routersName = 'app/routers'


def routerName(_path):
    routerModulePath = os.path.dirname(__file__) + '/' + routersName + '/'
    return _path.replace(routerModulePath, '').replace('.py', '')


def register_routers(app, directory=f"{routersName}", parent_prefix=''):
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            subdirectory_prefix = f"{parent_prefix}/{entry}" if parent_prefix else entry
            register_routers(app, full_path, subdirectory_prefix)
        elif entry.endswith('.py') and entry != '__init__.py':
            module_name = os.path.splitext(entry)[0]
            uripath = f"{directory}/{module_name}" if parent_prefix else f"{directory}/{module_name}"
            module_path = uripath.replace("/", '.')
            module = import_module(module_path)

            # 모듈이 APIRouter 인스턴스를 가지고 있는지 확인
            if isinstance(module.router, APIRouter):
                app.include_router(module.router, prefix=f"{uripath.replace(routersName, '')}")
            else:
                print(f"Skipping {module_path}: No APIRouter instance found.")
