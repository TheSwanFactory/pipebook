import pytest
from .conftest import *

@pytest.fixture
def doc():
    app = get_app()
    doc = app.load_demo()
    return doc

def test_yaml(doc):
    assert doc.yaml

def test_run(doc):
    assert len(doc.pipe.data) == 0
    doc.pipe.run()
    assert len(doc.pipe.data) > 0
