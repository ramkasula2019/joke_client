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
        if self._base_url is None:
            self._base_url = "https://sv443.net/jokeapi/v2/joke"
        #print(self._base_url)
        return self._base_url   

    @property
    def category(self):
        """_category (str or list/tuple/set) : Category of joke to fetch"""
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

        valid_category = ["Programming", "Miscellaneous", "Dark"]
        # test if value is string
        if isinstance(value, str):
            if value in valid_category:
                self._category = value
            elif value == "Any":
                self._category = value
            else:
                raise ValueError ("Invalid Category")
        # Check if value is list / set / tuple
        elif isinstance(value, (tuple, set, list)):
            if set(value).issubset(valid_category):
                self._category = ",".join(value)
            else:
                # if passed tuple/list/set has no valid value in category
                raise ValueError (
                        "Argument should be of type {}".format(valid_category)
                        )
        elif value is None:
            self._category = None
        else:
            raise TypeError (" Argument should be of type String or tuple or list or set")

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, value):
        valid_flags = [ 
            "nsfw",
            "religious",
            "political",
            "racist",
            "sexist"
            ]

        if value is None:
            self._flags = value
        elif isinstance (value,str):
            if value in valid_flags:
                self._flags = value
            else:
                raise ValueError(f"flags must be one of : {valid_flags}")
        elif isinstance (value, (tuple, set , list)):
            if set(value).issubset(valid_flags):
                self._flags = ",".join(value)
            else:
                raise ValueError (f"flags list must be among: {valid_flags}")
        else:
            raise TypeError ("Unxpected flag type. Must be String/Tuple/List/Set")

'''
jc = JokeClient()
jc.base_url
'''
    