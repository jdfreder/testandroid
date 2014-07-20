"""Contains TestBackend class"""
import backend

class TestBackend(backend.BackendBase):
    """Interface to a help backend."""

    def search(self, query):
        """This will return a list of page ids.  Page ids will be GUID (globally 
        unique identifier) strings."""
        print('DEBUG: search %s' % query)
        
        return ['page1', 'page2']

    def enumerate_categories(self):
        """This will return a list of category names."""
        print('DEBUG: query categories')
        
        return ['Category 1', 'Category 2']

    def get_category_description(self, category_name):
        """This will return a user friendly description string."""
        print('DEBUG: getting cat. description for "%s"' % category_name)
        
        if category_name == 'Category 1':
            return 'This category is awesome!'
        elif category_name == 'Category 2':
            return 'This category sucks!'

    def enumerate_category(self, category_name):
        """Return a list of all of the page ids within that specific category."""
        print('DEBUG: enumerating cat. for "%s"' % category_name)
        
        if category_name == 'Category 1':
            return ['page1']
        elif category_name == 'Category 2':
            return ['page1', 'page2']

    def get_topic_description(self, page_id):
        """Get the user friendly topic description."""
        print('DEBUG: getting page desc. for "%s"' % category_name)
        
        if category_name == 'page1':
            return "This is the first page!"
        elif category_name == 'page2':
            return "This is the second page!"

    def get_topic_rst(self, page_id):
        """Get the topic RST text."""
        print('DEBUG: getting page RST for "%s"' % category_name)
        
        if category_name == 'page1':
            return "Hello world!"
        elif category_name == 'page2':
            return "Goodbye world!"
