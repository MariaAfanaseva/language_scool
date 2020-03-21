from copy import deepcopy


class Address:

    def __init__(self):
        self.country = None
        self.region = None
        self.city = None
        self.street = None
        self.house_number = None
        self.apartment_number = None
        self.postcode = None

    def __str__(self):
        ret = ''
        for attr in self.__dict__:
            value = self.__getattribute__(attr)
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
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.e_mail = e_mail
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'{self.person_id}, {self.name}, {self.surname}, ' \
            f'{self.e_mail}, {self.phone}, {self.address}'


class Student(Person):

    def __init__(self, person_id, name, surname,  e_mail, phone,
                 address, language_level,
                 courses_id):
        super().__init__(person_id, name, surname,  e_mail, phone, address)
        self.language_level = language_level
        self.courses_id = courses_id

    def __str__(self):
        return f'level: {self.language_level}, courses_id: {self.courses_id}'


class Teacher(Person):

    def __init__(self, person_id, name, surname,  e_mail, phone, address,
                 languages, courses_id, diplomas, salary):
        super().__init__(person_id, name, surname,  e_mail, phone, address)
        self.languages = languages
        self.courses_id = courses_id
        self.diplomas = diplomas
        self.salary = salary

    def __str__(self):
        return f'languages: {self.languages}, courses_id: {self.courses_id}, ' \
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
        self.course_id = None
        self.language = None
        self.level = None
        self.price = None
        self.teachers = []
        self.students = []
        self.address = None
        self.books = None

    def __str__(self):
        ret = ''
        for attr in self.__dict__:
            value = self.__getattribute__(attr)
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


class ChangeCourse:

    @staticmethod
    def add_student(course, new_student_id):
        students = course.students
        students.append(new_student_id)
        setattr(course, 'students', students)

    @staticmethod
    def add_teacher(course, new_teacher_id):
        new_teachers = course.teachers
        new_teachers.append(new_teacher_id)
        setattr(course, 'teachers', new_teachers)


class ChangeStudent:

    @staticmethod
    def change_name(student, new_name):
        setattr(student, 'name', new_name)
        return student

    @staticmethod
    def add_course(student, new_course_id):
        new_courses = student.courses_id
        new_courses.append(new_course_id)
        setattr(student, 'courses_id', new_courses)
        return student


class ChangeTeacher:

    @staticmethod
    def change_name(teacher, new_name):
        setattr(teacher, 'name', new_name)

    @staticmethod
    def add_course(teacher, new_course_id):
        new_courses = teacher.courses_id
        new_courses.append(new_course_id)
        setattr(teacher, 'courses_id', new_courses)


class ChangeFacade:

    """Pattern Facade"""

    def __init__(self):
        self.change_student = ChangeStudent()
        self.change_teacher = ChangeTeacher()
        self.change_course = ChangeCourse()

    def add_teacher_to_course(self, course, teacher):
        teacher_id = teacher.person_id
        self.change_course.add_teacher(course, teacher_id)
        course_id = course.course_id
        self.change_teacher.add_course(teacher, course_id)

    def add_student_to_course(self, course, student):
        student_id = student.person_id
        self.change_course.add_student(course, student_id)
        course_id = course.course_id
        self.change_student.add_course(student, course_id)


def copy_course(course):
    """Pattern prototype"""
    return deepcopy(course)
