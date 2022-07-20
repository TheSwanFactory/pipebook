from pipebook import __version__
from .conftest import *

def test_version():
    assert __version__ == '0.1.0'

def test_app():
    app = PipeBookApp(APP_NAME, APP_ID)
    assert app

def test_registry():
    app = PipeBookApp(APP_NAME, APP_ID)
    app.startup()
    assert app.registry

def test_yaml():
    assert PKG_ID
    path = path_package(PKG_ID)
    assert PKG_ID in str(path)
    pipe_path = path_resource(PKG_ID, PIPE_FOLDER)
    assert pipe_path
