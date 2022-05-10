from encode import *
from fileapi import *
import sys

sys.path.append('C:/aydin-os/apps')

def py_to_app(filepath: str,app_name: str):
    filepath = "C:/aydin-os/" + filepath
    f = open(filepath, "r")
    content = f.read()
    f.close()
    execontent = swap(content)
    create_dir(f"/apps/{app_name}")
    write_file(f"/apps/{app_name}/main.app", execontent)
    return execontent

def execute_app(app: str):
    f = deswap(open(f"C:/aydin-os/root/apps/{app}/main.app").read())
    __globals__ = globals()
    exec(f)

def apps():
    apps = read_file('/system/apps/apps.list').split('\n')
    return apps
