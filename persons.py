from order_pay import Order, CreditCard, CreditCardPayment
from sqlite_db.mappers.update_database import DomainObject


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


class Teacher(Person, DomainObject):

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
