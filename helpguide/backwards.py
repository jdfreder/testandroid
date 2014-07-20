"""Contains BackwardsPage class"""
from kivy.uix.button import Button

from page import PageBase

class BackwardsPage(PageBase):
    """A page that allows you to go back to the parent page."""

    def __init__(self, app, history):
        """Constructor

        Parameters
        ----------
        app: Kivy App instance
        history: PageBase instance
            Reference to the history so we can return to it."""
        super(BackwardsPage, self).__init__(app)

        if not isinstance(history, list):
            history = [history]
        self.history = history
        def on_back_press(instance):
            self.hide()
            self.history.pop().show()

        back_button = Button(text='Back', size_hint=(None, None))
        back_button.height = '50px'
        back_button.bind(on_press=on_back_press)
        self.body.add_widget(back_button)
    
    def show(self, history=None):
        """Shows the page."""
        if history is not None:
            if not isinstance(history, list):
                history = [history]
            self.history = history
        super(BackwardsPage, self).show()
