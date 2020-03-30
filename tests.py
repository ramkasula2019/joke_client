""" Include test cases for joke client """

import unittest
from client import JokeClient

class JokeClientTestCase(unittest.TestCase):

    # For each test case set up is run to create new object of JokeClient
    def setUp(self):
        self.joke_client = JokeClient()

    def test_if_joke_client_is_instance_properly(self):
        self.assertIsInstance(self.joke_client, JokeClient)

    def test_base_url_is_valid(self):
        self.assertEqual(self.joke_client.base_url, "https://sv443.net/jokeapi/v2/joke")


if __name__ == "__main__":
    unittest.main()        


