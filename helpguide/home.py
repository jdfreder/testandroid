"""Contains the Home Page of the App."""
from page import PageBase
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from test import TestBackend

class HomePage(PageBase):
    """HomePage of the App.

    This is the first page that the user will see."""

    def __init__(self, *pargs, **kwargs):
        """Constructor"""
        # Call the base.
        super(HomePage, self).__init__(*pargs, **kwargs)

        # Load the backend
        self.backend = TestBackend()

        # Create a body manually, overriding the default.
        self.body = AnchorLayout(anchor_x='center', anchor_y='center')

        grid = GridLayout(cols=2, row_default_height=20, size_hint=(0.9, None))
        grid.height = '100px'
        self.body.add_widget(grid)

        def on_enter(sender):
            self._on_search(sender, self.query.text)
        self.query = TextInput(text='', multiline=False, hint_text='Type here...')
        self.query.bind(on_text_validate=on_enter)
        def on_button_press(sender):
            self._on_search(self.query, self.query.text)
        search = Button(text='Search!', width=50, height=50)
        search.bind(on_press=on_button_press)
        grid.add_widget(self.query)
        grid.add_widget(search)

    def _on_search(self, sender, value):
        """Called when the user trys to search."""
        query = value
        self.query.text = ''
        print(self.backend.search(query))
