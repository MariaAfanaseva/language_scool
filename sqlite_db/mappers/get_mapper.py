from sqlite_db.mappers.teacher_mapper import TeacherMapper
from persons import Teacher


class MapperRegistry:

    def __init__(self, connection):
        self.connection = connection
        self.teacher_mapper = TeacherMapper

    def get_mapper(self, obj):
        if isinstance(obj, Teacher):
            return TeacherMapper(self.connection)
        else:
            raise Exception(f'There is no view for an object of type {type(obj)}')
