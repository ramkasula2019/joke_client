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

    # @base_url.setter
    # def base_url(self, value):
    #     if value == None:
    #         self._base_url = value

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

    @property
    def response_format(self):
        return self._response_format
    
    @response_format.setter
    def response_format(self, value):
        valid_response_format = ["xml", "yaml", "json", "text"]
        if isinstance(value, str):
            if value in valid_response_format:
                self._response_format = value
            else:
                raise ValueError("The response format should be one of {}".format(valid_response_format))
        else:
            raise TypeError("Response format must be of type string")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        valid_joke_type = ["single",  "twopart"]

        if isinstance(value, str):
            if value not in valid_joke_type:
                raise ValueError ("the value shoule be one of {}".format(valid_joke_type))
            else:
                self._type = value
        else:
            raise TypeError("Plz provide string type")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if isinstance(value, int):
            if value in range (0,170):
                self._id = value 
            else:
                raise ValueError ("The value should be in between 0 and 169")
        else:
            raise TypeError ("The id should be integer")

    
    def joke(self):
        "fetches a joke from api and return them"
        url =  "{0}/{1}".format(self._base_url,self.category)       
        response = requests.get(url = url)
        if response.status_code ==200:
            if response.text:
                return response.json()
            return None

# jc = JokeClient(category=['Programming','Dark'])
# jc1 = JokeClient(category='Programming')
# jc.base_url
# json_response = jc.joke()
# print(type(json_response))
# if(isinstance(json_response,dict)):
#     print("yes")
# else:
#     print("NO")

    