from copy import deepcopy


class Person:

    def __init__(self, name, surname,  e_mail, phone, address):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'{self.name}, {self.surname}, ' \
            f'{self.e_mail}, {self.phone}, {self.address}'


class Student(Person):

    def __init__(self, name, surname,  e_mail, phone,
                 address, student_number, language_level,
                 curses):
        super().__init__(name, surname,  e_mail, phone, address)
        self.student_number = student_number
        self.language_level = language_level
        self.curses = curses

    def __str__(self):
        return f'number: {self.student_number} ' \
            f'level: {self.language_level}, courses: {self.curses}'


class Teacher(Person):

    def __init__(self, name, surname,  e_mail, phone, address,
                 languages, diplomas, salary):
        super().__init__(name, surname,  e_mail, phone, address)
        self.languages = languages
        self.diplomas = diplomas
        self.salary = salary

    def __str__(self):
        return f'languages: {self.languages}, ' \
            f'diplomas: {self.diplomas}, salary: {self.salary}'


class Course:

    def __init__(self, language, level, price,
                 teachers, students,
                 address, books):
        self.language = language
        self.level = level
        self.price = price
        self.teachers = teachers
        self.students = students
        self.address = address
        self.books = books

    def __str__(self):
        return f'{self.language}, {self.level}, ' \
            f'price: {self.price}, teachers: {self.teachers}, ' \
            f'students: {self.students}, address: {self.address}, ' \
            f'books: {self.books}'


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
                ret += f'{attr}: {value} '
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


class PersonFactory:

    """ Pattern FATORY METHOD """

    person_types = {
        'teacher': Teacher,
        'student': Student
    }

    @staticmethod
    def create_person(person_type, name,
                      surname,  e_mail, phone, address, **kwargs):
        person_class = PersonFactory.person_types[person_type]
        person = person_class(name=name, surname=surname,
                              e_mail=e_mail, phone=phone,
                              address=address, **kwargs)
        return person


class Change:

    def __init__(self, item, **kwargs):
        self.item = item
        self.kwargs = kwargs

    def change_data(self):
        for attr in self.kwargs:
            setattr(self.item, attr, self.kwargs[attr])
        return self.item


def copy_course(course):
    """Patten prototype"""
    return deepcopy(course)
