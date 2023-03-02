"""
Module used to make the tests of
the database.
"""

# ---- Imports ----
import unittest
import database as db
import copy
import helpers
# ---- End Imports ----

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clients.l = [
            db.Client('15J', 'Marta', 'Perez'),
            db.Client('48H', 'Manuel', 'Lopez'),
            db.Client('28Z', 'Ana', 'Garcia')
        ]

    def test_search_client(self):
        existent_client = db.Clients.search('15J')
        nonexistent_client = db.Clients.search('99X')
        self.assertIsNotNone(existent_client)
        self.assertIsNone(nonexistent_client)

    def test_create_client(self):
        new_client = db.Clients.create('06S', 'Ingold', 'Aguilar')
        self.assertEqual(len(db.Clients.l), 4)
        self.assertEqual(new_client.ssn, '06S')
        self.assertEqual(new_client.name, 'Ingold')
        self.assertEqual(new_client.last_name, 'Aguilar')
        self.assertIsNotNone(new_client)

    def test_modify_client(self):
        client_to_modify = copy.copy(db.Clients.search('28Z'))
        modified_client = db.Clients.modify('28Z', 'Mariana', 'Garcia')
        self.assertEqual(client_to_modify.name, 'Ana')
        self.assertEqual(modified_client.name, 'Mariana')

    def test_delete_client(self):
        deleted_client = db.Clients.delete('48H')
        researched_client = db.Clients.search('48H')  # should be None.
        self.assertEqual(deleted_client.ssn, '48H')
        self.assertIsNone(researched_client)

    def test_valid_ssn(self):
        self.assertTrue(helpers.valid_ssn('00A', db.Clients.l))
        self.assertFalse(helpers.valid_ssn('232323S', db.Clients.l))
        self.assertFalse(helpers.valid_ssn('F35', db.Clients.l))
        self.assertFalse(helpers.valid_ssn('4F2', db.Clients.l))
        self.assertFalse(helpers.valid_ssn('48H', db.Clients.l))