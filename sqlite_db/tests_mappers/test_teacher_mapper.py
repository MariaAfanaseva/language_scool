import unittest
import sqlite3
from classes import AddressBuilder, PersonFactory
from sqlite_db.mappers.teacher_mapper import TeacherMapper
from sqlite_db.create_sqlite_db import DatabaseBuilder


class TestTeacherMapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        builder = DatabaseBuilder('../test_db.sqlite')
        builder.create_database()

    def setUp(self):
        self.connect = sqlite3.connect('../test_db.sqlite')
        self.teacher_mapper = TeacherMapper(self.connect)

    def test_work(self):

        #  insert
        address = AddressBuilder().set_city('London').set_street('Putina').build()
        person_factory = PersonFactory()
        new_teacher = person_factory.create_person(
            'teacher', None, 'TestTest 1',
            'Test 1', 'test@mail.ru', 9009, address,
            id_teacher=None, salary=2000,
            languages='Italian, English',
            courses_id='1',
            diplomas='Test diploma 1'
        )
        self.teacher_mapper.insert(new_teacher)

        # count
        count = self.teacher_mapper.count()
        self.assertEqual(count, 2)

        # find
        teacher = self.teacher_mapper.find_by_id(2)
        self.assertEqual(teacher.surname, 'Test 1')
        self.assertEqual(teacher.id_teacher, 2)

        #  update
        address = teacher.address
        address.street = 'Lenon'
        address.postcode = 456248
        address.house_number = 5
        address.apartment_number = 23

        teacher.phone = 98956421
        teacher.salary = 5000
        teacher.address = address
        self.teacher_mapper.update(teacher)

        # find updated
        teacher = self.teacher_mapper.find_by_id(2)
        self.assertEqual(teacher.salary, 5000)
        self.assertEqual(teacher.phone, 98956421)

        # delete
        self.teacher_mapper.delete(teacher)

        # count
        count = self.teacher_mapper.count()
        self.assertEqual(count, 1)

    @classmethod
    def tearDownClass(cls):
        builder = DatabaseBuilder('../test_db.sqlite')
        builder.create_database()


if __name__ == '__main__':
    unittest.main()
