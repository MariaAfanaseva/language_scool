import unittest
import sqlite3
from sqlite_db.create_sqlite_db import DatabaseBuilder
from sqlite_db.mappers.unit_of_work import UnitOfWork
from sqlite_db.mappers.get_mapper import MapperRegistry
from persons import PersonFactory
from address import AddressBuilder
from sqlite_db.mappers.teacher_mapper import TeacherMapper


class TestUnityOfWork(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        builder = DatabaseBuilder('../test_db.sqlite')
        builder.create_database()

    def setUp(self):
        self.connect = sqlite3.connect('../test_db.sqlite')

    def test_add_new(self):
        UnitOfWork.new_current()
        self.update = UnitOfWork.get_current()
        self.update.set_mapper_registry(MapperRegistry(self.connect))
        person_factory = PersonFactory()
        address = AddressBuilder().set_country('Germany').set_city('Berlin').\
            set_street('Lenina').set_house_number(6).set_apartment_number(34).\
            set_postcode(456234).build()
        new_teacher = person_factory.create_person(
            'teacher', None, 'TestTest new',
            'Test new', 'test@mail.ru', 9009, address,
            id_teacher=None,
            languages='Italian, English',
            courses_id='1',
            diplomas='Test diploma new'
        )
        new_teacher.mark_new()
        UnitOfWork.get_current().commit()

        #  get teacher
        mapper = TeacherMapper(self.connect)
        self.assertLessEqual(mapper.count(), 2)
        teacher = mapper.find_by_id(2)
        self.assertEqual(teacher.name, 'TestTest new')

        # update
        teacher.name = 'Anna Test'
        teacher.mark_update()
        UnitOfWork.get_current().commit()
        teacher = mapper.find_by_id(2)
        self.assertEqual(teacher.name, 'Anna Test')

        # delete
        teacher.mark_removed()
        UnitOfWork.get_current().commit()
        self.assertLessEqual(mapper.count(), 1)

    @classmethod
    def tearDownClass(cls):
        builder = DatabaseBuilder('../test_db.sqlite')
        builder.create_database()


if __name__ == '__main__':
    unittest.main()
