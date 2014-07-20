"""Contains RichPage class"""
from __future__ import print_function
from kivy.uix.listview import ListView, CompositeListItem, ListItemButton, ListItemLabel
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.uix.label import Label
from kivy.uix.rst import RstDocument
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

from backwards import BackwardsPage

class RichPage(BackwardsPage):
    """A link of links to other pages."""
    singletons = {}

    @classmethod
    def get_page(cls, app, history, backend, page_id):
        if page_id not in cls.singletons:
            cls.singletons[page_id] = cls(app, history, backend, page_id)
        return cls.singletons[page_id]

    def __init__(self, app, history, backend, page_id):
        """Constructor

        Parameters
        ----------
        app: Kivy App instance
        history: PageBase instance
            Reference to the history so we can return to it.
        backend: BackendBase instance"""
        super(RichPage, self).__init__(app, history)
        self._backend = backend
        self._page_id = page_id

        self.contents = BoxLayout(orientation='vertical')
        self.body.add_widget(self.contents)

        self._richtext = RstDocument(text='', size_hint=(1., None), height=50)
        self.contents.add_widget(self._richtext)

        self._simple_list_adapter = SimpleListAdapter(
            data=[], 
            args_converter=self._render_link, 
            selection_mode='single', 
            cls=CompositeListItem)

        self.list_view = ListView(adapter=self._simple_list_adapter)
        self.contents.add_widget(self.list_view)

        title_float = FloatLayout()
        self.body.add_widget(title_float)
        title_anchor = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1., 1.), pos=(200., 30.))
        title_float.add_widget(title_anchor)
        self._title = Label(text='', size_hint=(None, None), markup=True)
        title_anchor.add_widget(self._title)

        self.reload()

    def reload(self):
        """Reloads the page's contents."""
        self._simple_list_adapter.data = self._backend.get_page_links(self._page_id) or []
        self._title.text = '[color=2299ff][size=40]  %s[/size][/color]' % self._backend.get_page_title(self._page_id) or ''
        contents = self._backend.get_page_contents(self._page_id) or ''
        self._richtext.text = contents

        # Try to be smart about the page layout.  Look at the number of lines in 
        # the contents.  If it's more than 4, assume the contents are the 
        # primary interest of this page and size the rich text accordingly, else
        # the links are the primary interest.
        lines = len(contents.split('\n'))
        if lines > 4:
            self._richtext.size_hint = (1., 0.8)
            self.list_view.size_hint = (1., 0.2)
            self._richtext.colors['background'] = 'eaeaea'
            self._richtext.colors['paragraph'] = '202020'
        else:
            self._richtext.size_hint = (1., None)
            self._richtext.height = 20 + lines * 20
            self.list_view.size_hint = (1., 1.)
            self._richtext.colors['background'] = '000000'
            self._richtext.colors['paragraph'] = '005599'


    def _render_link(self, row_index, link_page_id):
        def _on_open(list_adapter, *args):
            if not isinstance(self.history, list):
                new_history = [self.history, self]
            else:
                new_history = self.history + [self]
            RichPage.get_page(self.app, new_history, self._backend, link_page_id).show(new_history)
            self.hide()
        return {
            'text': link_page_id,
            'size_hint_y': None,
            'height': 25, 'index': row_index,
            'halign': 'left',
            'cls_dicts': [
                {
                    'cls': ListItemLabel,
                    'kwargs': {
                        'text': "[b]{0}[/b]".format(self._backend.get_page_title(link_page_id) or 'Untitled'),
                        'size_hint_x': 0.1,
                        'halign': 'left',
                        'markup': True
                    }
                }, {
                    'cls': ListItemLabel,
                    'kwargs': {
                        'text': "{0}".format(self._backend.get_page_subtitle(link_page_id) or ''),
                        'is_representing_cls': True,
                        'size_hint_x': 0.8,
                        'halign': 'left'
                    }
                }, {
                    'cls': ListItemButton,
                    'kwargs': { 'text': 'Open', 'on_press': _on_open, 'size_hint_x': 0.1}
                }
            ]}
