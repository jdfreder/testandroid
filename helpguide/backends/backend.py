"""Contains BackendBase class"""

class BackendBase(object):
    """Interface to a help backend."""

    def search(self, query):
        """This will return a list of page ids.  Page ids will be GUID (globally 
        unique identifier) strings."""
        pass

    def get_page_title(self, page_id):
        """Gets the title of a page."""
        pass

    def get_page_subtitle(self, page_id):
        """Gets the subtitle of a page."""
        pass

    def get_page_contents(self, page_id):
        """Get the topic contents text."""
        pass

    def get_page_links(self, page_id):
        """Get the pages that are linked to from the page."""
        pass

    def get_category_links(self, category):
        """Get list of pages for a given category."""
        pass
