import unittest
from classes import (Address, AddressBuilder, Person,
                     Student, Teacher, PersonFactory,
                     Course, CreateCourse,
                     copy_course, Manager)


class TestAddress(unittest.TestCase):

    def setUp(self):
        self.address = Address(1, 'Russia', '', 'Moscow',
                               'Lenina', '7', '45', '5664')

    def test_init(self):
        self.assertEqual(self.address.country, 'Russia')
        self.assertEqual(self.address.region, '')
        self.assertEqual(self.address.city, 'Moscow')
        self.assertEqual(self.address.street, 'Lenina')
        self.assertEqual(self.address.house_number, '7')
        self.assertEqual(self.address.apartment_number, '45')
        self.assertEqual(self.address.postcode, '5664')


class TestAddressBuilder(unittest.TestCase):

    def setUp(self):
        self.address_builder = AddressBuilder()

    def test_set_country(self):
        self.assertEqual(self.address_builder.set_country('Germany'),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.country, 'Germany')

    def test_set_region(self):
        self.assertEqual(self.address_builder.set_region('Bayern'),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.region, 'Bayern')

    def test_set_city(self):
        self.assertEqual(self.address_builder.set_city('Munich'),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.city, 'Munich')

    def test_set_street(self):
        self.assertEqual(self.address_builder.set_street('Rahel'),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.street, 'Rahel')

    def test_set_house_number(self):
        self.assertEqual(self.address_builder.set_house_number(5),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.house_number, 5)

    def test_set_apartment_number(self):
        self.assertEqual(self.address_builder.set_apartment_number(52),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.apartment_number, 52)

    def test_set_postcode(self):
        self.assertEqual(self.address_builder.set_postcode(85642),
                         self.address_builder)
        self.assertEqual(self.address_builder.address.postcode, 85642)


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_country('Russia').build()
        self.person = Person(1, 'Maria', 'Afanaseva',
                             'ff@gmail.com', 891678523, self.address)

    def test_init(self):
        self.assertEqual(self.person.id_person, 1)
        self.assertEqual(self.person.name, 'Maria')
        self.assertEqual(self.person.surname, 'Afanaseva')
        self.assertEqual(self.person.email, 'ff@gmail.com')
        self.assertEqual(self.person.phone, 891678523)
        self.assertEqual(self.person.address, self.address)


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_country('Russia').build()
        self.student = Student(2, 'Ivan', 'Ivanov',  'ivan@ivan', 895642,
                               self.address, 2, ['English B1'], [112])

    def test_init(self):
        self.assertEqual(self.student.id_person, 2)
        self.assertEqual(self.student.name, 'Ivan')
        self.assertEqual(self.student.surname, 'Ivanov')
        self.assertEqual(self.student.email, 'ivan@ivan')
        self.assertEqual(self.student.phone, 895642)
        self.assertEqual(self.student.address, self.address)
        self.assertEqual(self.student.language_level, ['English B1'])
        self.assertEqual(self.student.courses_id, [112])

    # def test_str(self):
    #     self.assertEqual(str(self.student), f"2, Ivan, Ivanov, "
    #                                         "ivan@ivan, 895642, country: Russia, , "
    #                                         "level: ['English B1'], "
    #                                         "courses_id: [112]")


class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Moscow').build()
        self.teacher = Teacher(3, 'Lala', 'Fafa',  'lala@fafa.com',
                               78956, self.address, 1,
                               ['English', 'german'], [13],
                               ['Manchester diploma'],
                               5000)

    def test_init(self):
        self.assertEqual(self.teacher.id_person, 3)
        self.assertEqual(self.teacher.name, 'Lala')
        self.assertEqual(self.teacher.surname, 'Fafa')
        self.assertEqual(self.teacher.email, 'lala@fafa.com')
        self.assertEqual(self.teacher.phone, 78956)
        self.assertEqual(self.teacher.address, self.address)
        self.assertEqual(self.teacher.languages, ['English', 'german'])
        self.assertEqual(self.teacher.courses_id, [13])
        self.assertEqual(self.teacher.diplomas, ['Manchester diploma'])
        self.assertEqual(self.teacher.salary, 5000)


class TestManager(unittest.TestCase):

    def setUp(self):
        self.manager = Manager(4, 'Ivan', 'Ivanov', 'iva@mail.ru',
                               9096, 'Kiev', 1, 'Lingoda', 1000)

    def test_init(self):
        self.assertEqual(self.manager.school, 'Lingoda')
        self.assertEqual(self.manager.salary, 1000)
        self.assertEqual(self.manager.surname, 'Ivanov')


class TestPersonFactory(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.person_factory = PersonFactory()

    def test_create_teacher(self):
        teacher = self.person_factory.create_person(
            'teacher', 5, 'Nana',
            'Li',  'nana@h', 9009, self.address,
            id_teacher=2, salary=2000,
            languages=['Italian', 'English'],
            courses_id=[12],
            diplomas=['Ranish diploma']
        )
        self.assertEqual(teacher.name, 'Nana')
        self.assertEqual(teacher.surname, 'Li')
        self.assertEqual(teacher.address, self.address)
        self.assertIsInstance(teacher, Teacher)
        with self.assertRaises(TypeError):
            self.person_factory.create_person(
                'teacher', 6, 'Nana',
                'Li', 'nana@h', 9009, self.address,
                id_teacher=2, salary=2000,
                languages=['Italian', 'English'], courses_id=[12],
                level=['Ranish diploma']  # need diplomas not level
            )

        with self.assertRaises(KeyError):
            self.person_factory.create_person(
                'professor', 7, 'Nana', 'Li', 'nana@h',
                # need teacher or student not professor
                '9009', self.address, salary=2000,
                languages=['Italian', 'English'],
                diplomas=['Ranish diploma'], id_student=1,
            )

    def test_create_student(self):
        student = self.person_factory.create_person(
            'student', 8, 'Mama',
            'Li', 'mama@h', 9009, self.address,
            language_level=['Italian A2', 'English B2'],
            courses_id=[56], id_student=3
        )
        self.assertEqual(student.name, 'Mama')
        self.assertEqual(student.surname, 'Li')
        self.assertEqual(student.address, self.address)
        self.assertIsInstance(student, Student)
        with self.assertRaises(TypeError):
            self.person_factory.create_person(
                'student', 9, 'Nana',
                'Li', 'nana@h', 9000, self.address,
                language_level=['Italian A2', 'English B2'],
                diplomas=['Ranish diploma']  # need courses not diplomas
            )


class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course = Course()
        self.id_course = self.course.id_course

    def test_init(self):
        self.assertEqual(self.course.language, None)
        self.assertEqual(self.course.level, None)
        self.assertEqual(self.course.price, None)
        self.assertEqual(self.course.teachers, [])
        self.assertEqual(self.course.students, [])
        self.assertEqual(self.course.address, None)
        self.assertEqual(self.course.books, [])

    def test_add_teacher(self):
        self.course.add_teacher(11)
        self.assertIn(11, self.course.teachers)

    def test_add_student(self):
        self.course.add_student(18)
        self.assertIn(18, self.course.students)

    def test_str(self):
        self.assertEqual(str(self.course), f'id_course: {self.id_course}, ')

    def tearDown(self):
        Course.id -= 1


class TestCourseBuilder(unittest.TestCase):

    def setUp(self):
        self.course_builder = CreateCourse()
        self.address = AddressBuilder().set_city('Munich').build()

    def test_set_language(self):
        self.assertEqual(self.course_builder.set_language('german'),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.language, 'german')

    def test_set_level(self):
        self.assertEqual(self.course_builder.set_level('B1'),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.level, 'B1')

    def test_set_price(self):
        self.assertEqual(self.course_builder.set_price(200),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.price, 200)

    def test_set_teachers_id_id(self):
        self.assertEqual(self.course_builder.set_teachers_id([1, 2]),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.teachers, [1, 2])

    def test_set_students_id(self):
        self.assertEqual(self.course_builder.set_students_id([4, 5, 6]),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.students, [4, 5, 6])

    def test_set_address(self):
        self.assertEqual(self.course_builder.set_address(self.address),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.address, self.address)

    def test_set_books(self):
        self.assertEqual(self.course_builder.set_books('Gek'),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.books, 'Gek')

    def tearDown(self):
        Course.id -= 1


class TestCopy(unittest.TestCase):

    def setUp(self):
        self.course = CreateCourse().set_language('English').\
            set_address('Moscow').set_teachers_id([4]).\
            set_students_id([5, 8]).set_books('No')
        self.new_course = copy_course(self.course)

    def test_copy_course(self):
        self.assertNotEqual(self.course, self.new_course)
        self.assertEqual(self.course.course.language,
                         self.new_course.course.language)
        self.assertEqual(str(self.course.course), str(self.new_course.course))

    def tearDown(self):
        Course.id -= 1


if __name__ == '__main__':
    unittest.main()
