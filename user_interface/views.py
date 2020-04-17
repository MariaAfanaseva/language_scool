import sqlite3
from sqlite_db.mappers.teacher_mapper import TeacherMapper
from user_interface.render import render
from sqlite_db.update_database import UpdateDatabase


class Views:

    def __init__(self):
        _db_path = '../sqlite_db/school_db.sqlite'
        _connection = sqlite3.connect(_db_path, check_same_thread=False)
        self.teacher_mapper = TeacherMapper(_connection)
        self.update_db = UpdateDatabase(_connection)

    def teachers_list_view(self, request):
        teachers = self.teacher_mapper.all()
        return render('teachers.html', object_list=teachers)

    def add_teacher_view(self, request):
        if request['method'] == 'GET':
            return render('add_teacher.html')
        else:
            params = request['params']
            # print(params)
            #  get data
            name = params[b'name'][0].decode(encoding='utf-8')
            surname = params[b'surname'][0].decode(encoding='utf-8')
            email = params[b'email'][0].decode(encoding='utf-8')
            phone = params[b'phone'][0].decode(encoding='utf-8')
            country = params[b'country'][0].decode(encoding='utf-8')
            city = params[b'city'][0].decode(encoding='utf-8')
            languages = params[b'languages'][0].decode(encoding='utf-8')
            courses_id = params[b'courses'][0].decode(encoding='utf-8')
            diplomas = params[b'diplomas'][0].decode(encoding='utf-8')
            self.update_db.save_teacher(name, surname, email, phone,
                                        country, city, languages,
                                        courses_id, diplomas)
            return render('add_teacher_confirm.html')
