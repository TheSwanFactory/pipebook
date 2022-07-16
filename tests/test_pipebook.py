from pipebook import __version__
from .conftest import *
from fridaay import PKG_ID

def test_version():
    assert __version__ == '0.1.0'

def test_app():
    app = PipeBookApp(APP_NAME, APP_ID)
    assert app

def test_registry():
    app = PipeBookApp(APP_NAME, APP_ID)
    app.startup()
    assert app.registry
