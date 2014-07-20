"""Contains the Home Page of the App."""
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from page import PageBase
from rich import RichPage
from backends.test import TestBackend
from backends.special import SpecialBackend

class HomePage(PageBase):
    """HomePage of the App.

    This is the first page that the user will see."""

    def __init__(self, app):
        """Constructor"""
        # Call the base.
        super(HomePage, self).__init__(app)

        # Load the backend
        self.backend = SpecialBackend(TestBackend())

        # Create a body manually, overriding the default.
        self.body = AnchorLayout(anchor_x='center', anchor_y='center')
        stack_layout = StackLayout(size_hint=(0.95, 0.6))
        self.body.add_widget(stack_layout)

        text_layout =  BoxLayout(anchor_x='left', anchor_y='center', size_hint=(0.8, None))
        text_layout.height = '35px'
        stack_layout.add_widget(text_layout)

        def on_enter(sender):
            self._on_search(sender, self.query.text)
        self.query = TextInput(text='', multiline=False, hint_text='Type here...')
        self.query.bind(on_text_validate=on_enter)
        text_layout.add_widget(self.query)


        button_layout =  BoxLayout(anchor_x='right', anchor_y='center', size_hint=(0.2, None))
        button_layout.height = '35px'
        stack_layout.add_widget(button_layout)

        def on_search_press(sender):
            self._on_search(self.query, self.query.text)
        search = Button(text='Search!')
        search.width = '50px'
        search.bind(on_press=on_search_press)
        button_layout.add_widget(search)

        self.search_results = RichPage.get_page(app, [self], self.backend, 'search')

        def on_category_press(sender):
            RichPage.get_page(app, [self], self.backend, 'categories').show(self)
            self.hide()
        category = Button(text='Categories', size_hint=(None, None), height='35px')
        category.width = '100px'
        category.bind(on_press=on_category_press)        
        self.body.add_widget(category)

    def _on_search(self, sender, value):
        """Called when the user trys to search."""
        query = value
        self.query.text = ''

        self.backend.cached_search(query)
        self.search_results.reload()

        self.hide()
        self.search_results.show(self)
