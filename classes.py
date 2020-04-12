from copy import deepcopy
from order_pay import Order, CreditCard, CreditCardPayment


class Address:

    def __init__(self, id_address, country, region, city, street,
                 house_number, apartment_number, postcode):
        self.id_address: int = id_address
        self.country: str = country
        self.region: str = region
        self.city: str = city
        self.street: str = street
        self.house_number: str = house_number
        self.apartment_number: str = apartment_number
        self.postcode: str = postcode

    def __str__(self):
        ret = ''
        for value in self.__dict__.values():
            ret += f'{value},'
        return ret


class AddressBuilder:

    """ Pattern Builder """

    def __init__(self):
        self.address = Address(None, '', '', '', '', '', '', '')

    def set_id_address(self, id_address):
        self.address.id_address = id_address
        return self

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

    def __init__(self, id_person, name, surname,  email, phone, address):
        self.id_person: int = id_person
        self.name: str = name
        self.surname: str = surname
        self.email: str = email
        self.phone: int = phone
        self.address = address

    def __str__(self):
        return f'{self.id_person}, {self.name}, {self.surname}, ' \
            f'{self.email}, {self.phone}, {self.address}'


class Student(Person):

    def __init__(self, id_person, name, surname,  email, phone,
                 address, id_student, language_level,
                 courses_id):
        super().__init__(id_person, name, surname,  email, phone, address)
        self.id_student: int = id_student
        self.language_level: str = language_level
        self.courses_id: str = courses_id

    def __str__(self):
        str_person = super().__str__()
        return f'{str_person}, level: {self.language_level}, ' \
            f'courses_id: {self.courses_id}'


class Teacher(Person):

    def __init__(self, id_person, name, surname,  email, phone, address,
                 id_teacher, languages, courses_id, diplomas, salary):
        super().__init__(id_person, name, surname,  email, phone, address)
        self.id_teacher: int = id_teacher
        self.languages: str = languages
        self.courses_id: str = courses_id
        self.diplomas: str = diplomas
        self.salary: float = salary

    def __str__(self):
        str_person = super().__str__()
        return f'{str_person}, languages: {self.languages}, courses_id: {self.courses_id}, ' \
            f'diplomas: {self.diplomas}, salary: {self.salary}'


class Manager(Person):

    def __init__(self, id_person, name, surname,
                 email, phone, address, id_manager, school, salary):
        super().__init__(id_person, name, surname,
                         email, phone, address)
        self.id_manager: int = id_manager
        self.salary: float = salary
        self.school = school

        self.order = None
        self.payment = None

    def create_order(self, customer):
        self.order = Order(customer)

    def add_course_to_order(self, course):
        self.order.add_item(course)

    def add_credit_card(self, number, owner, code):
        credit_card = CreditCard(number, owner, code)
        self.payment = CreditCardPayment(credit_card)

    def pay_order(self):
        email = self.order.customer.email
        phone = self.order.customer.phone
        order_number = self.order.order_number
        if self.payment and self.order.items:
            print(self.order.pay(self.payment))
            self.school.send_message('PAY', phone, email, order_number)
            self.order = None
            self.payment = None

    def __str__(self):
        str_person = super().__str__()
        return f'{str_person}, school: {self.school}, salary: {self.salary}'


class PersonFactory:

    """ Pattern FACTORY METHOD """

    person_types = {
        'teacher': Teacher,
        'student': Student,
        'manager': Manager
    }

    @staticmethod
    def create_person(person_type, id_person, name, surname,
                      email, phone, address, **kwargs):
        person_class = PersonFactory.person_types[person_type]
        person = person_class(id_person=id_person, name=name,
                              surname=surname,
                              email=email, phone=phone,
                              address=address, **kwargs)
        return person


class Course:

    id = 0

    def __init__(self):
        Course.id += 1
        self.id_course: int = Course.id
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


class CreateCourse:

    """ Pattern Builder """

    def __init__(self):
        self.course = Course()

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


def copy_course(course):
    """Pattern prototype"""
    return deepcopy(course)
