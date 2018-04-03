import unittest
import requests
from requests import Session
from flask_sqlalchemy import SQLAlchemy
#from app import db

class TestComputationServer(unittest.TestCase):

    def test_valid_post(self):
        '''
        POST an HTTP request with a valid expression to the server. Examine the response and
        confirm that the correct answer is returned.
        '''
        expression = "1 + 1"
        value = 2

        details = {"text":expression}

        req = requests.post('http://localhost:5000/add', data = details )

        index = req.text
        index = index.split("<li>")
        index = index[1].split("=")

        self.assertEqual(value, int(index[0]))

    def test_expression_database(self):
        '''
        Establish a connection to the database directly and verify that the string you sent
        has been correctly stored in the database.
        '''
        expression = "1 + 1"
        # details = {"text":expression}
        # req = requests.post("http://localhost:5000/add", data = details)

        ex = Expression.query(text).first()

        self.assertEqual(expression, ex)

    def test_invalid_post(self):
        '''
        POST an HTTP request with an invalid expression to the server. Examine the response
        and confirm that an error is raised.
        '''
        expression = "1 + a"

        details = {"text":expression}

        req = requests.post('http://localhost:5000/add', data = details )

        self.assertRaises(SomeException)

    def test_database_entry(self):
        '''
        Confirm that no more rows have been added to the database since the last valid expression
        was sent to the server.
        '''
        rows = Expression.query().count()

        self.assertEqual(1, rows)

if __name__ == "__main__":

    expression = "1 + 1"
    value = 2

    details = {"text":expression}

    req = requests.post('http://localhost:5000/add', data = details )

    index = req.text
    index = index.split("<li>")
    index = index[1].split("=")
    self.assertEqual(value, int(index[0]))
    #unittest.main()

