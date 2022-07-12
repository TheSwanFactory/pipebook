from random import choice
from collections import defaultdict, namedtuple
from fridaay import Pipe

import toga
from toga.sources import TreeSource
from toga.sources.tree_source import Node
from toga.constants import COLUMN, ROW
from toga.style import Pack

class FrameViewer():

    def __init__(self, app, name, frame):
        self.app = app
        self.name = name
        self.frame = frame
        self.startup()

    def startup(self):
        # Set up main window

        self.app.window_counter += 1
        self.window = toga.Window(title=self.name)
        # Both self.windows.add() and self.windows += work:
        self.app.windows += self.window

        # Label to show responses.
        self.label = toga.Label('Ready.', style=Pack(padding=10))

        self.table = toga.Table(
            headings=self.frame.columns,
            data=self.frame,
            multiple_select=True,
            style=Pack(flex=1, padding_left=5),
        )

        # Outermost box
        outer_box = toga.Box(
            children=[self.table, self.label],
            style=Pack(
                flex=1,
                direction=COLUMN,
            )
        )

        # Add the content on the main window
        self.window.content = outer_box

        # Show the main window
        self.window.show()
