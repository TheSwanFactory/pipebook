import toga
from toga.constants import COLUMN, ROW
from toga.sources import Source

class FrameData(Source):

    def __init__(self, raw):
        super().__init__()
        self.raw = raw
        self.columns = raw.columns

    def __len__(self):
        return len(self.raw)

    def __getitem__(self, index):
        return self.raw.iloc[index]

    def index(self, entry):
        return self.raw.index(entry)
