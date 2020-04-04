from send_info import CreateNotifier


class LanguageSchool:

    def __init__(self):
        self.courses: list = []
        self.teachers: list = []
        self.students: list = []
        self.email_notifier = CreateNotifier.get_notifier('EMAIL', 'languageSchool@gmail.com')
        self.sms_notifier = CreateNotifier.get_notifier('SMS', 500)

    def add_person(self, person_type, person):
        if person_type == 'teacher':
            self.teachers.append(person)
        elif person_type == 'student':
            self.students.append(person)

    def add_course(self, course):
        self.courses.append(course)

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
