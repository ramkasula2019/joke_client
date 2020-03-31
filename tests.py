""" Include test cases for joke client """

import unittest
from client import JokeClient

class JokeClientTestCase(unittest.TestCase):

    # For each test case set up is run to create new object of JokeClient
    def setUp(self):
        self.joke_client = JokeClient()

    def test_if_joke_client_is_instance_properly(self):
        self.assertIsInstance(self.joke_client, JokeClient)

    def test_joke_client_if_base_url_is_valid(self):
        self.assertEqual(self.joke_client.base_url, "https://sv443.net/jokeapi/v2/joke")

    def test_joke_client_if_category_is_valid(self):
        # List of valid category
        valid_category = ["Programming", "Miscellaneous", "Dark"]

        # List of invalid category
        invalid_category = ["Programming", "Invalid"]

        # Assert when data list is valid. Here we set current local valid_category to category
        # so following line itself produce value error if invalid category assign in valid_category list
        self.joke_client.category = valid_category
        for category in valid_category:
            self.assertIn(category, self.joke_client.category)

        # Assert when data is invalid
        with self.assertRaises(ValueError):
            self.joke_client.category = invalid_category

        # Assert when string with invalid category other than 'Any'
        with self.assertRaises(ValueError):
            self.joke_client.category = "Invalid"

        # Better to think that "Any" is assigned through our client.py and asserting that if it is truely assigned.
        self.joke_client.category = "Any"
        self.assertEqual(self.joke_client.category, "Any")

        self.joke_client.category = "Programming"
        self.assertEqual(self.joke_client.category, "Programming")

        # Assert when category type is invalid
        with self.assertRaises(TypeError):
            self.joke_client.category = 10

    def test_joke_client_if_flgas_is_valid(self):
        valid_flag_list = [ "nsfw", "religious", "political", "racist", "sexist"]
        invalid_flag_list = [ "invalid", "sssreligious"]

        # Assert when flags is None
        self.joke_client.flags = None
        self.assertFalse(self.joke_client.flags)

        self.joke_client.flags = "religious"
        self.assertIn(self.joke_client.flags, "religious")
        
        with self.assertRaises(ValueError):
            self.joke_client.flags = "Invalid"
        
        self.joke_client.flags = valid_flag_list
        for flags in valid_flag_list:
            self.assertIn(flags, valid_flag_list)

        with self.assertRaises(ValueError):
            self.joke_client.flags = invalid_flag_list

        with self.assertRaises(TypeError):
            self.joke_client.flags = 10








if __name__ == "__main__":
    unittest.main()        


