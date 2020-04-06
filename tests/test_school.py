import unittest
from classes import AddressBuilder
from school import LanguageSchool


class TestLanguageSchool(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.school = LanguageSchool('Lingoda', 'Berlin')

    def test_create_person(self):
        self.school.create_person('teacher', 'Nana',
                                   'Li',  'nana@h', '9009', self.address, salary=2000,
                                   languages=['Italian', 'English'],
                                   courses_id=[12],
                                   diplomas=['Ranish diploma'])

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


if __name__ == '__main__':
    unittest.main()
