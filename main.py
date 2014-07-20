from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from helpguide.home import HomePage


class HelpGuideApp(App):

    def build(self):
        self.root = FloatLayout()
        self.home = HomePage(self)
        self.home.show()
        return self.root

    def remove_widget(self, widget):
        """Remove a widget from the app."""
        self.root.remove_widget(widget)

    def add_widget(self, widget):
        """Add a widget to the app."""
        self.root.add_widget(widget)


HelpGuideApp().run()
