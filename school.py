from classes import PersonFactory, CreateCourse
from create_message import (PayMessage, NewsMessage,
                            EmailMessage, SMSMessage)


class LanguageSchool:

    """Pattern Facade"""

    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.courses: list = []
        self.teachers: list = []
        self.students: list = []
        self.managers: list = []
        self.phone = phone
        self.email = email

        self.message_pay = PayMessage('Pay course',
                                      'Course paid successfully. Order number ')
        self.news_message = NewsMessage('News', 'New courses for you')

        self.set_sender()

    def set_sender(self):
        send_email = EmailMessage(school_email=self.email)
        send_phone = SMSMessage(school_phone=self.phone)

        self.message_pay.attach(send_email)
        self.message_pay.attach(send_phone)
        self.news_message.attach(send_email)

    def create_person(self, person_type, id_person, name,
                      surname, e_mail, phone, id_address, **kwargs):
        person = PersonFactory().create_person(person_type, id_person, name,
                                               surname, e_mail, phone, id_address, **kwargs)
        if person_type == 'teacher':
            self.teachers.append(person)
        elif person_type == 'student':
            self.students.append(person)
        elif person_type == 'manager':
            self.managers.append(person)

    def create_course(self, language, level, price, address, books,
                      teachers=None, students=None):
        course = CreateCourse().set_language(language) \
            .set_price(price).set_level(level). \
            set_address(address).set_books(books)
        if teachers:
            course.set_teachers_id(teachers)
        if students:
            course.set_students_id(students)
        course = course.build()
        self.courses.append(course)

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

    def send_message(self, message_type, phone, email, data):
        if message_type == 'PAY':
            self.message_pay.data = phone, email, data
        elif message_type == 'NEWS':
            self.news_message.data = phone, email, data
