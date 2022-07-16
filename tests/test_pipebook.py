from pipebook import __version__
from .conftest import *

def test_version():
    assert __version__ == '0.1.0'

def test_app():
    app = PipeBookApp(APP_NAME, APP_ID)
