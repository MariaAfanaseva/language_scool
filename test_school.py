import unittest
from classes import AddressBuilder, SchoolManager


class TestLanguageSchool(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.manager = SchoolManager

    def test_create_person(self):
        self.manager.create_person('teacher', 'Nana',
                                   'Li',  'nana@h', '9009', self.address, salary=2000,
                                   languages=['Italian', 'English'],
                                   courses_id=[12],
                                   diplomas=['Ranish diploma'])

        teacher = self.manager.school.teachers[0]
        self.assertNotEqual(self.manager.school.teachers, [])
        self.assertEqual(teacher.name, 'Nana')

    def test_create_course(self):
        self.manager.create_course('English', 'A1', 400, self.address,
                                   'English A1 London School', teachers=[4])
        course = self.manager.school.courses[0]
        self.assertNotEqual(self.manager.school.courses, [])
        self.assertEqual(course.language, 'English')
        self.assertEqual(course.teachers, [4])


if __name__ == '__main__':
    unittest.main()
