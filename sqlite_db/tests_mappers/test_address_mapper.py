import unittest
import sqlite3
from sqlite_db.mappers.teacher_mapper import TeacherMapper
from sqlite_db.mappers.address_mapper import AddressMapper
from sqlite_db.create_sqlite_db import DatabaseBuilder
from classes import AddressBuilder


class TestTeacherMapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        builder = DatabaseBuilder('../test_db.sqlite')
        builder.create_database()

    def setUp(self):
        self.connect = sqlite3.connect('../test_db.sqlite')
        self.teacher_mapper = TeacherMapper(self.connect)

    def test_work(self):
        # create new
        address = AddressBuilder().set_city('Moscow').build()
        mapper = AddressMapper(self.connect)
        mapper.insert(address)

        # find by id
        self.assertEqual(mapper.id_address, 2)
        address = mapper.find_by_id(2)
        self.assertEqual(address.city, 'Moscow')
        self.assertEqual(address.country, '')

    @classmethod
    def tearDownClass(cls):
        builder = DatabaseBuilder('../test_db.sqlite')
        builder.create_database()


if __name__ == '__main__':
    unittest.main()
