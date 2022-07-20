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
    doc.pipe.run()
    data = doc.pipe.data
    assert len(data) > 0
