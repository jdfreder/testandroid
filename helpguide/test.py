"""Contains TestBackend class"""
import backend

class TestBackend(backend.BackendBase):
    """Interface to a help backend."""

    pages = {
        'page1': {
            'title': 'Hot',
            'subtitle': 'This page is awesome!',
            'contents': 'This is a long description of heat and thermodynamics.',
            'links': ['page2'],
        },
        'page2': {
            'title': 'Cold',
            'subtitle': "Why read this?  Don't.",
            'contents': 'Cold is a lack of heat.',
            'links': ['page1'],
        },
    }

    def search(self, query):
        """This will return a list of page ids.  Page ids will be GUID (globally 
        unique identifier) strings."""
        return TestBackend.pages.keys()

    def get_page_title(self, page_id):
        """Gets the title of a page."""
        if page_id in TestBackend.pages:
            return TestBackend.pages[page_id]['title']
        else:
            return 'Page not found'

    def get_page_subtitle(self, page_id):
        """Gets the subtitle of a page."""
        if page_id in TestBackend.pages:
            return TestBackend.pages[page_id]['subtitle']
        else:
            return '...'

    def get_page_contents(self, page_id):
        """Get the topic contents text."""
        if page_id in TestBackend.pages:
            return TestBackend.pages[page_id]['contents']
        else:
            return ''

    def get_page_links(self, page_id):
        """Get the pages that are linked to from the page."""
        if page_id in TestBackend.pages:
            return TestBackend.pages[page_id]['links']
        else:
            return []
