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

    def __len__(self):
        return len(self.raw)

    def __getitem__(self, index):
        print('__getitem__',index)
        series = self.raw.iloc[index]
        keys = np.append(series.index, INDEX_KEY)
        values = np.append(series, index)
        return tuple(values)
        #return tuple(zip(keys, values))

    def index(self, column_name):
        print('index',column_name)
        return self.columns.index(column_name)
