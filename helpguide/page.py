"""Contains a PageBase class that all the GUI pages will inherit from."""
from kivy.uix.stacklayout import StackLayout

class PageBase(object):
    """Base Page"""

    def __init__(self, app):
        """Constructor"""
        if not hasattr(self, 'body'):
            self.body = StackLayout(padding=[10,10,10,10])
        self.app = app
        self._visible = False

    @property
    def visible(self):
        """True if the page is visible, False otherwise."""
        return self._visible
    @visible.setter
    def visible(self, value):
        """True if the page is visible, False otherwise."""
        if self._visible != value:
            if value:
                self.show()
            else:
                self.hide()
    
    def show(self):
        """Shows the page."""
        if not self._visible:
            self.app.add_widget(self.body)
            self._visible = True

    def hide(self):
        """Hides the page."""
        if self._visible:
            self.app.remove_widget(self.body)
            self._visible = False
