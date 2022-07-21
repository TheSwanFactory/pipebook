import pytest
from .conftest import *
from collections.abc import Hashable

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

def test_frames(doc):
    doc.pipe.run()
    for name, dataset in doc.pipe.data.items():
        print(name)
        #fv = FrameView(doc.app, name, dataset)
        frame = FrameData(dataset)
        assert frame
        assert frame.__len__() > 1
        item0 = frame.__getitem__(0)
        print(item0)
        assert isinstance(item0, Hashable)
