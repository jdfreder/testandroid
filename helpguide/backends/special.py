"""Contains SpecialBackend class"""
import backend

class SpecialBackend(backend.BackendBase):
    """Backend that has special category and search pages builtin."""

    def __init__(self, backend):
        """Constructor"""
        self._backend = backend
        self._categories = {
            'categories': {
                'title': 'Categories',
                'contents': 'List of categories:',
                'links': ['html', 'css']
            },
            'html': {
                'title': 'HTML',
                'subtitle': 'Web page layout',
                'contents': 'HTML topics:',
                'links': self.get_category_links('html')
            },
            'css': {
                'title': 'CSS',
                'subtitle': 'Web page styling',
                'contents': 'CSS topics:',
                'links': self.get_category_links('html')
            }
        }
        self._search_results = []
        self._search_query = ''

    def search(self, query):
        """This will return a list of page ids.  Page ids will be GUID (globally 
        unique identifier) strings."""
        return self._backend.search(query)

    def get_page_title(self, page_id):
        """Gets the title of a page."""
        if page_id == 'search':
            return 'Search results'
        elif page_id in self._categories:
            return self._categories[page_id]['title']
        else:
            return self._backend.get_page_title(page_id)

    def get_page_subtitle(self, page_id):
        """Gets the subtitle of a page."""
        if page_id == 'search':
            return 'Search results'
        elif page_id in self._categories:
            return self._categories[page_id]['subtitle']
        else:
            return self._backend.get_page_subtitle(page_id)

    def get_page_contents(self, page_id):
        """Get the topic contents text."""
        if page_id == 'search':
            return self._pad_contents_text('Search results for "%s":' % self._search_query)
        elif page_id in self._categories:
            contents = self._categories[page_id]['contents']
            if 'padded_contents' in self._categories[page_id] and self._categories[page_id]['padded_contents']:
                return self._pad_contents_text(contents)
            else:
                return contents
        else:
            return self._backend.get_page_contents(page_id)

    def get_page_links(self, page_id):
        """Get the pages that are linked to from the page."""
        if page_id == 'search':
            return self._search_results
        elif page_id in self._categories:
            return self._categories[page_id].get('links', [])
        else:
            return self._backend.get_page_links(page_id)

    def get_category_links(self, category):
        """Get list of pages for a given category."""
        return self._backend.get_category_links(category)

    def cached_search(self, query):
        """Perform a search and cache the results."""
        self._search_query = query
        self._search_results = self.search(query)

    def _pad_contents_text(self, text):
        """Pad the contents text so it aligns with the page title."""
        # Append 28 nbsp characters to the front of the text to indent it.
        # I know this is lame, but it's the only why to do this cleanly
        # at the time of writing.
        return u'\xA0' * 28 + unicode(text)
