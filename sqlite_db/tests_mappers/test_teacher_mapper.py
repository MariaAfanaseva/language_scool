import unittest
import sqlite3
from classes import AddressBuilder, PersonFactory
from sqlite_db.mappers.teacher_mapper import TeacherMapper


class TestTeacherMapperInsert(unittest.TestCase):

    def setUp(self):
        self.connect = sqlite3.connect('../school_db.sqlite')
        self.teacher_mapper = TeacherMapper(self.connect)
        self.address = AddressBuilder().set_city('London').set_street('Putina').build()
        self.person_factory = PersonFactory()
        self.teacher = self.person_factory.create_person(
                    'teacher', None, 'TestTest',
                    'Test',  'test@mail.ru', 9009, self.address,
                    id_teacher=2, salary=2000,
                    languages='Italian, English',
                    courses_id=12,
                    diplomas='Test diploma'
                )

    def test_insert(self):
        self.teacher_mapper.insert(self.teacher)

    def test_find_by_id(self):
        teacher = self.teacher_mapper.find_by_id(2)
        self.assertEqual(teacher.surname, 'Test')
        self.assertEqual(teacher.id_teacher, 2)


class TestTeacherMapperUpdate(unittest.TestCase):

    def setUp(self):
        self.connect = sqlite3.connect('../school_db.sqlite')
        self.teacher_mapper = TeacherMapper(self.connect)
        address = AddressBuilder().set_id_address(2).set_city('London'). \
            set_street('Putina').set_street('Lenon').set_house_number(5). \
            set_apartment_number(23).build()
        person_factory = PersonFactory()
        self.teacher = person_factory.create_person(
            'teacher', 2, 'TestTest',
            'Test', 'testtestovich@mail.ru',
            98956421, address,
            id_teacher=2, salary=5000,
            languages='Italian, English',
            courses_id='12, 15',
            diplomas='Test diploma'
        )

    def test_update(self):
        self.teacher_mapper.update(self.teacher)

    #  run separately
    # def test_delete(self):
    #     self.teacher_mapper.delete(self.teacher)


class TestTeacherMapperCount(unittest.TestCase):

    def setUp(self):
        self.connect = sqlite3.connect('../school_db.sqlite')
        self.teacher_mapper = TeacherMapper(self.connect)

    def test_count(self):
        result = self.teacher_mapper.count()
        print(result)


if __name__ == '__main__':
    unittest.main()
