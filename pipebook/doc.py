from random import choice
from .data import obj2tree
from toga.sources import TreeSource
from toga.sources.tree_source import Node

from collections import defaultdict, namedtuple

import toga
from toga.constants import COLUMN, ROW
from toga.style import Pack

class PipeBookDoc():

    # Table callback functions
    def on_select_handler(self, widget, node):
        if node is not None and node.name:
            self.label.text = f'You selected node: {node.name}'
            self.btn_remove.enabled = True
        else:
            self.label.text = 'No node selected'
            self.btn_remove.enabled = False

    # Button callback functions
    def insert_handler(self, widget, **kwargs):
        self.tree.data

    def remove_handler(self, widget, **kwargs):
        selection = self.tree.selection
        if selection.title:
            self.tree.data.remove(selection)

    def startup(self):
        # Set up main window
        self.doc_window = toga.Window(title=self.name)

        # Label to show responses.
        self.label = toga.Label('Ready.', style=Pack(padding=10))

        source = obj2tree()
        self.tree = toga.Tree(
            headings=source._accessors,
            style=Pack(flex=1)
        )
        self.tree.data = source

        # Buttons
        btn_style = Pack(flex=1, padding=10)
        self.btn_insert = toga.Button('Insert Row', on_press=self.insert_handler, style=btn_style)
        self.btn_remove = toga.Button('Remove Row', enabled=False, on_press=self.remove_handler, style=btn_style)
        self.btn_box = toga.Box(children=[self.btn_insert, self.btn_remove], style=Pack(direction=ROW))

        # Outermost box
        outer_box = toga.Box(
            children=[self.btn_box, self.tree, self.label],
            style=Pack(
                flex=1,
                direction=COLUMN,
            )
        )

        # Add the content on the main window
        self.doc_window.content = outer_box

        # Show the main window
        self.doc_window.show()
