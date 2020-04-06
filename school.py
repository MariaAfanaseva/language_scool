from send_info import CreateNotifier
from classes import PersonFactory, CreateCourse


class LanguageSchool:

    """Pattern Facade"""

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.courses: list = []
        self.teachers: list = []
        self.students: list = []
        self.managers: list = []
        self.email_notifier = CreateNotifier.get_notifier('EMAIL', 'languageSchool@gmail.com')
        self.sms_notifier = CreateNotifier.get_notifier('SMS', 500)

    def create_person(self, person_type, name,
                      surname, e_mail, phone, address, **kwargs):
        person = PersonFactory().create_person(person_type, name,
                                               surname, e_mail, phone, address, **kwargs)
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

    def send_message(self, message_type, phone, email, order_number):
        if message_type == 'PAY':
            if email:
                self.email_notifier.notify(email, 'Pay course',
                                           'Congratulations!'
                                           f'You paid for the order number {order_number}.')
            if phone:
                self.sms_notifier.notify(phone, 'Pay course',
                                         'Congratulations!'
                                         f'You paid for the order number {order_number}.')
