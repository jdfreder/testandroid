"""Contains BackendBase class"""

class BackendBase(object):
    """Interface to a help backend."""

    def search(self, query):
        """This will return a list of page ids.  Page ids will be GUID (globally 
        unique identifier) strings."""
        pass

    def enumerate_categories(self):
        """This will return a list of category names."""
        pass

    def get_category_description(self, category_name):
        """This will return a user friendly description string."""
        pass

    def enumerate_category(self, category_name):
        """Return a list of all of the page ids within that specific category."""
        pass

    def get_topic_description(self, page_id):
        """Get the user friendly topic description."""
        pass

    def get_topic_rst(self, page_id):
        """Get the topic RST text."""
        pass
