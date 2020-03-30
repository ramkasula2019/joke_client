""" Simple client to fetch joke from api"""

import requests


__author__ = "Ram Kasula"
__email__ = "ram.kasula@cotiviti.com"
__status__ = "dev"
__version__ = "0.1"

class JokeClient:
    """ Joke Client
    Attributes:
        _category (str or list/tuple/set) : Category of joke to fetch
        _flags (list/tuple/set, optional) : Flag unwanted jokes
        _response_format(str) : response format of joke, default is json
        _type(str, optional) : two part or single part joke type
        _search(str) : search keyword 
        _id (str, optional) : id of the joke, range = (0, 169)
    """

    def __init__(
        self,
        category = "Any",
        flags = None,
        response_format = "json",
        type = None,
        search = None,
        id = None
        ):
        # Private variable do not modify
        self._base_url = None
        self._category = None,
        self._flags = None,
        self._response_format = None,
        self._type = None,
        self._search = None,
        self._id = None

        # Attribute
        self.category = category

    @property
    def base_url(self):
        if _base_url is None:
            _base_url = "https://sv443.net/jokeapi/v2/joke"
        return self._base_url   

    @property
    def category(self):
        """_category (str or list/tuple/set) : Category of joke to fetch"""
        return self._category

    @category.setter
    def category(self, value):
        self._category = value


    