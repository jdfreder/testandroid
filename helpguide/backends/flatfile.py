"""Contains FlatfileBackend class"""
from glob import glob
import json
import pprint
from helpguide.backends import backend


class FlatfileBackend(backend.BackendBase):
    """Interface to a help backend."""

    def __init__(self):
        print('hello world')
        self.listOfAllJSONPages = glob('data/guide/*.json')

    def search(self, query):
        """This will return a list of page ids.  Page ids will be GUID (globally 
        unique identifier) strings."""

        #searches database for all ids
        searchresults = []
        for x in self.listOfAllJSONPages:
            with open(x) as f:
                read = json.load(f)
                del read['links']
                newlist = read.values()
                newstring = ' '.join(newlist)
                if query.upper() in newstring.upper():
                    searchresults.append(x)

        return searchresults
        #returns list of page ids related to query


    def get_page_title(self, page_id):
        """Gets the title of a page."""
        with open(page_id) as f:
            return json.load(f)['title']


    def get_page_subtitle(self, page_id):
        """Gets the subtitle of a page."""
        with open(page_id) as f:
            return json.load(f)['subtitle']

    def get_page_contents(self, page_id):
        """Get the topic contents."""
        with open(page_id) as f:
            return json.load(f)['contents']

    def get_page_links(self, page_id):
        """Get the pages that are linked to from the page."""
        with open(page_id) as f:
            return json.load(f)['links']

    def get_category_links(self, category):
        """Get list of pages for a given category."""
        searchresults = []
        for x in self.listOfAllJSONPages:
            with open(x) as f:
                read = json.load(f)
                if category.upper() == read["category"].upper():
                    searchresults.append(x)

        return searchresults
