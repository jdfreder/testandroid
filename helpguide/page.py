"""Contains a PageBase class that all the GUI pages will inherit from."""
from kivy.uix.boxlayout import BoxLayout

class PageBase(object):
    """Base Page"""

    def __init__(self, app):
        """Constructor"""
        if not hasattr(self, 'body'):
            self.body = BoxLayout(orientation='vertical')
        self._app = app
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
            self._app.add_widget(self.body)
            self._visible = True

    def hide(self):
        """Hides the page."""
        if self._visible:
            self._app.remove_widget(self.body)
            self._visible = False
