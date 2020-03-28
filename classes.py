from copy import deepcopy


class Address:

    def __init__(self):
        self.country: str = None
        self.region: str = None
        self.city: str = None
        self.street: str = None
        self.house_number: int = None
        self.apartment_number: int = None
        self.postcode: int = None

    def __str__(self):
        ret = ''
        for attr, value in self.__dict__.items():
            if value:
                ret += f'{attr}: {value}, '
        return ret


class AddressBuilder:

    """ Pattern Builder """

    def __init__(self):
        self.address = Address()

    def set_country(self, country):
        self.address.country = country
        return self

    def set_region(self, region):
        self.address.region = region
        return self

    def set_city(self, city):
        self.address.city = city
        return self

    def set_street(self, street):
        self.address.street = street
        return self

    def set_house_number(self, house_number):
        self.address.house_number = house_number
        return self

    def set_apartment_number(self, apartment_number):
        self.address.apartment_number = apartment_number
        return self

    def set_postcode(self, postcode):
        self.address.postcode = postcode
        return self

    def build(self):
        return self.address


class Person:

    def __init__(self, person_id, name, surname,  e_mail, phone, address):
        self.person_id: int = person_id
        self.name: str = name
        self.surname: str = surname
        self.e_mail: str = e_mail
        self.phone: str = phone
        self.address = address

    def __str__(self):
        return f'{self.person_id}, {self.name}, {self.surname}, ' \
            f'{self.e_mail}, {self.phone}, {self.address}'


class Student(Person):

    def __init__(self, person_id, name, surname,  e_mail, phone,
                 address, language_level,
                 courses_id):
        super().__init__(person_id, name, surname,  e_mail, phone, address)
        self.language_level: str = language_level
        self.courses_id: list = courses_id

    def add_course(self, course_id):
        self.courses_id.append(course_id)

    def __str__(self):
        str_person = super().__str__()
        return f'{str_person}, level: {self.language_level}, ' \
            f'courses_id: {self.courses_id}'


class Teacher(Person):

    def __init__(self, person_id, name, surname,  e_mail, phone, address,
                 languages, courses_id, diplomas, salary):
        super().__init__(person_id, name, surname,  e_mail, phone, address)
        self.languages: list = languages
        self.courses_id: list = courses_id
        self.diplomas: list = diplomas
        self.salary: float = salary

    def add_course(self, course_id):
        self.courses_id.append(course_id)

    def __str__(self):
        str_person = super().__str__()
        return f'{str_person}, languages: {self.languages}, courses_id: {self.courses_id}, ' \
            f'diplomas: {self.diplomas}, salary: {self.salary}'


class PersonFactory:

    """ Pattern FACTORY METHOD """

    person_types = {
        'teacher': Teacher,
        'student': Student
    }

    @staticmethod
    def create_person(person_type, person_id, name,
                      surname,  e_mail, phone, address, **kwargs):
        person_class = PersonFactory.person_types[person_type]
        person = person_class(person_id=person_id, name=name,
                              surname=surname,
                              e_mail=e_mail, phone=phone,
                              address=address, **kwargs)
        return person


class Course:

    def __init__(self):
        self.course_id: int = None
        self.language: str = None
        self.level: str = None
        self.price: float = None
        self.teachers: list = []
        self.students: list = []
        self.address: str = None
        self.books: list = []

    def add_teacher(self, teacher_ip):
        self.teachers.append(teacher_ip)

    def add_student(self, student_ip):
        self.students.append(student_ip)

    def __str__(self):
        ret = ''
        for attr, value in self.__dict__.items():
            if value:
                ret += f'{attr}: {value}, '
        return ret


class CourseBuilder:

    """ Pattern Builder """

    def __init__(self):
        self.course = Course()

    def set_course_id(self, course_id):
        self.course.course_id = course_id
        return self

    def set_language(self, language):
        self.course.language = language
        return self

    def set_level(self, level):
        self.course.level = level
        return self

    def set_price(self, price):
        self.course.price = price
        return self

    def set_teachers_id(self, teachers):
        self.course.teachers = teachers
        return self

    def set_students_id(self, students):
        self.course.students = students
        return self

    def set_address(self, address):
        self.course.address = address
        return self

    def set_books(self, books):
        self.course.books = books
        return self

    def build(self):
        return self.course


class SchoolManager(Person):

    """Pattern Facade"""

    def __init__(self, person_id, name, surname,
                 e_mail, phone, address, work_address, salary):
        super().__init__(person_id, name, surname,
                         e_mail, phone, address)
        self.work_address: str = work_address
        self.salary: float = salary

    @staticmethod
    def add_teacher_to_course(course, teacher):
        teacher_id = teacher.person_id
        course.add_teacher(teacher_id)
        course_id = course.course_id
        teacher.add_course(course_id)

    @staticmethod
    def add_student_to_course(course, student):
        student_id = student.person_id
        course.add_student(student_id)
        course_id = course.course_id
        student.add_course(course_id)


def copy_course(course):
    """Pattern prototype"""
    return deepcopy(course)
