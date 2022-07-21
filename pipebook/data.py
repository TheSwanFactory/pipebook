from collections import namedtuple
import toga
from toga.constants import COLUMN, ROW
from toga.sources import Source
import numpy as np
INDEX_KEY="#"

class FrameData(Source):

    def __init__(self, raw):
        super().__init__()
        self.raw = raw
        self.columns = raw.columns.to_list()
        self.struct = namedtuple("row", ['index']+self.columns)
        self.data = [self.struct(*r) for r in self.raw.itertuples()]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        print('__getitem__',index)
        return self.data[index]

    def index(self, entry):
        print('index',entry)
        return self.data.index(entry)
