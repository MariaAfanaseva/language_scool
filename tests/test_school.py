import unittest
from classes import AddressBuilder
from school import LanguageSchool


class TestLanguageSchool(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.school = LanguageSchool('Lingoda', 'Berlin',
                                     800, 'lingoda@gmail.com')

    def test_create_person(self):
        self.school.create_person('teacher', 3, 'Nana',
                                   'Li',  'nana@h', '9009', 2, salary=2000,
                                   id_teacher=2,
                                   languages='Italian, English',
                                   courses_id='12',
                                   diplomas='Ranish diploma')

        teacher = self.school.teachers[0]
        self.assertNotEqual(self.school.teachers, [])
        self.assertEqual(teacher.name, 'Nana')

    def test_create_course(self):
        self.school.create_course('English', 'A1', 400, self.address,
                                   'English A1 London School', teachers=[4])
        course = self.school.courses[0]
        self.assertNotEqual(self.school.courses, [])
        self.assertEqual(course.language, 'English')
        self.assertEqual(course.teachers, [4])

    def test_work_send_message(self):
        self.school.send_message('PAY', 891645782, 'mari@maol.ru', 5)
        self.school.send_message('NEWS', 854622176, 'all@mail.ru',
                                 'latin course and spain course')


if __name__ == '__main__':
    unittest.main()
