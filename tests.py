import unittest
from classes import (Address, AddressBuilder, Person,
                     Student, Teacher, PersonFactory,
                     Course, CourseBuilder,
                     copy_course, SchoolManager)


class TestAddress(unittest.TestCase):

    def setUp(self):
        self.address = Address()

    def test_init(self):
        self.assertEqual(self.address.country, None)
        self.assertEqual(self.address.region, None)
        self.assertEqual(self.address.city, None)
        self.assertEqual(self.address.street, None)
        self.assertEqual(self.address.house_number, None)
        self.assertEqual(self.address.apartment_number, None)
        self.assertEqual(self.address.postcode, None)

    def test_str(self):
        self.assertEqual(str(self.address), '')


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

    def test_str(self):
        self.assertEqual(str(self.address_builder.set_country('USA').build()),
                         'country: USA, ')
        self.assertEqual(str(self.address_builder.set_house_number(10).
                             set_street('Pop').set_city('Berlin').build()),
                         'country: USA, city: Berlin, '
                         'street: Pop, house_number: 10, ')


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_country('Russia').build()
        self.person = Person(1, 'Maria', 'Afanaseva',
                             'ff@gmail.com', '454-334', self.address)

    def test_init(self):
        self.assertEqual(self.person.person_id, 1)
        self.assertEqual(self.person.name, 'Maria')
        self.assertEqual(self.person.surname, 'Afanaseva')
        self.assertEqual(self.person.e_mail, 'ff@gmail.com')
        self.assertEqual(self.person.phone, '454-334')
        self.assertEqual(self.person.address, self.address)

    def test_str(self):
        self.assertEqual(str(self.person),
                         '1, Maria, Afanaseva, ff@gmail.com, 454-334, '
                         'country: Russia, ')


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_country('Russia').build()
        self.student = Student(2, 'Ivan', 'Ivanov',  'ivan@ivan', '9090',
                               self.address, ['English B1'], [112])

    def test_init(self):
        self.assertEqual(self.student.person_id, 2)
        self.assertEqual(self.student.name, 'Ivan')
        self.assertEqual(self.student.surname, 'Ivanov')
        self.assertEqual(self.student.e_mail, 'ivan@ivan')
        self.assertEqual(self.student.phone, '9090')
        self.assertEqual(self.student.address, self.address)
        self.assertEqual(self.student.language_level, ['English B1'])
        self.assertEqual(self.student.courses_id, [112])

    def test_add_course(self):
        self.student.add_course(57)
        self.assertIn(57, self.student.courses_id)

    def test_str(self):
        self.assertEqual(str(self.student), "2, Ivan, Ivanov, "
                                            "ivan@ivan, 9090, country: Russia, , "
                                            "level: ['English B1'], "
                                            "courses_id: [112]")


class TestTeacher(unittest.TestCase):

    def setUp(self):
        self.address = Address()
        self.teacher = Teacher(3, 'Lala', 'Fafa',  'lala@fafa.com',
                               '7980-678', self.address,
                               ['English', 'german'], [13],
                               ['Manchester diploma'],
                               5000)

    def test_init(self):
        self.assertEqual(self.teacher.person_id, 3)
        self.assertEqual(self.teacher.name, 'Lala')
        self.assertEqual(self.teacher.surname, 'Fafa')
        self.assertEqual(self.teacher.e_mail, 'lala@fafa.com')
        self.assertEqual(self.teacher.phone, '7980-678')
        self.assertEqual(self.teacher.address, self.address)
        self.assertEqual(self.teacher.languages, ['English', 'german'])
        self.assertEqual(self.teacher.courses_id, [13])
        self.assertEqual(self.teacher.diplomas, ['Manchester diploma'])
        self.assertEqual(self.teacher.salary, 5000)

    def test_add_course(self):
        self.teacher.add_course(57)
        self.assertIn(57, self.teacher.courses_id)

    def test_str(self):
        self.assertEqual(str(self.teacher), "3, Lala, Fafa, lala@fafa.com, "
                                            f"7980-678, {self.address}, languages: ['English', 'german'], courses_id: [13], "
                                            "diplomas: ['Manchester diploma'], salary: 5000")


class TestPersonFactory(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.person_factory = PersonFactory()

    def test_create_teacher(self):
        teacher = self.person_factory.create_person(
            'teacher', 4, 'Nana',
            'Li',  'nana@h', '9009', self.address, salary=2000,
            languages=['Italian', 'English'],
            courses_id=[12],
            diplomas=['Ranish diploma']
        )
        self.assertEqual(teacher.person_id, 4)
        self.assertEqual(teacher.name, 'Nana')
        self.assertEqual(teacher.surname, 'Li')
        self.assertEqual(teacher.address, self.address)
        self.assertIsInstance(teacher, Teacher)
        with self.assertRaises(TypeError):
            self.person_factory.create_person(
                'teacher', 5, 'Nana',
                'Li', 'nana@h', '9009', self.address, salary=2000,
                languages=['Italian', 'English'], courses_id=[12],
                level=['Ranish diploma']  # need diplomas not level
            )

        with self.assertRaises(KeyError):
            self.person_factory.create_person(
                'professor', 6, 'Nana', 'Li', 'nana@h',
                # need teacher or student not professor
                '9009', self.address, salary=2000,
                languages=['Italian', 'English'],
                diplomas=['Ranish diploma']
            )

    def test_create_student(self):
        student = self.person_factory.create_person(
            'student', 7, 'Mama',
            'Li', 'mama@h', '9009', self.address,
            language_level=['Italian A2', 'English B2'],
            courses_id=[56]
        )
        self.assertEqual(student.name, 'Mama')
        self.assertEqual(student.surname, 'Li')
        self.assertEqual(student.address, self.address)
        self.assertIsInstance(student, Student)
        with self.assertRaises(TypeError):
            self.person_factory.create_person(
                'student', 8, 'Nana',
                'Li', 'nana@h', '9009', self.address,
                language_level=['Italian A2', 'English B2'],
                diplomas=['Ranish diploma']  # need courses not diplomas
            )


class TestCourse(unittest.TestCase):

    def setUp(self):
        self.course = Course()

    def test_init(self):
        self.assertEqual(self.course.course_id, None)
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
        self.assertEqual(str(self.course), '')


class TestCourseBuilder(unittest.TestCase):

    def setUp(self):
        self.course_builder = CourseBuilder()
        self.address = AddressBuilder().set_city('Munich').build()

    def test_set_course_id(self):
        self.assertEqual(self.course_builder.set_course_id(123),
                         self.course_builder)
        self.assertEqual(self.course_builder.course.course_id, 123)

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


class TestCopy(unittest.TestCase):

    def setUp(self):
        self.course = CourseBuilder().set_course_id(5).\
            set_language('English').\
            set_address('Moscow').set_teachers_id([4]).\
            set_students_id([5, 8]).set_books('No')
        self.new_course = copy_course(self.course)

    def test_copy_course(self):
        self.assertNotEqual(self.course, self.new_course)
        self.assertEqual(self.course.course.course_id,
                         self.new_course.course.course_id)
        self.assertEqual(str(self.course.course), str(self.new_course.course))


class TestSchoolManager(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.teacher = PersonFactory().create_person(
            'teacher', 10, 'Eva',
            'Lop', 'eva@h', '5000-56', self.address,
            languages=['Italian', 'English'],
            courses_id=[56],
            diplomas=['Rom diploma'],
            salary=5000
        )
        self.student = PersonFactory().create_person(
            'student', 9, 'Mama',
            'Li', 'mama@h', '9009', self.address,
            language_level=['Italian A2', 'English B2'],
            courses_id=[56]
        )
        self.course = CourseBuilder().set_course_id(45).set_language('English').\
            set_level('B2').set_address(self.address).set_price(300).build()
        self.manager = SchoolManager(19, 'Ivan', 'Ivanov', 'iva@mail.ru',
                                     '9096', 'Kiev', 'Sing street', 1000)

    def test_init(self):
        self.assertEqual(self.manager.work_address, 'Sing street')
        self.assertEqual(self.manager.salary, 1000)
        self.assertEqual(self.manager.surname, 'Ivanov')

    def test_add_teacher_to_course(self):
        self.manager.add_teacher_to_course(self.course, self.teacher)
        self.assertIn(10, self.course.teachers)
        self.assertIn(45, self.teacher.courses_id)

    def test_add_student_to_course(self):
        self.manager.add_student_to_course(self.course, self.student)
        self.assertIn(9, self.course.students)
        self.assertIn(45, self.student.courses_id)


if __name__ == '__main__':
    unittest.main()
