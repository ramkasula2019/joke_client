""" Include test cases for joke client """

import unittest
from client import JokeClient

class JokeClientTestCase(unittest.TestCase):

    # For each test case set up is run to create new object of JokeClient
    def setUp(self):
        self.joke_client = JokeClient()

    def test_if_joke_client_is_instance_properly(self):
        self.assertIsInstance(self.joke_client, JokeClient)

if __name__ == "__main__":
    unittest.main()        


