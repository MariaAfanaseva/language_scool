from copy import deepcopy


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
