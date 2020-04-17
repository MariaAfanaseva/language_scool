from persons import PersonFactory
from sqlite_db.mappers.address_mapper import AddressMapper
from sqlite_db.mappers.person_mapper import PersonMapper
from sqlite_db.mappers.errors import (DbDeleteException,
                                      RecordNotFoundException,
                                      DbUpdateException)


class TeacherMapper:

    """Pattern data mapper"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.id_teacher = None
        self.addr_mapper = AddressMapper(self.connection)
        self.person_mapper = PersonMapper(self.connection)

    def _create_address(self, new_teacher):
        address = new_teacher.address
        self.addr_mapper.insert(address)
        id_address = self.addr_mapper.id_address
        return id_address

    def _create_person(self, new_teacher):
        self.person_mapper.insert(new_teacher)
        id_person = self.person_mapper.id_person
        return id_person

    def insert(self, new_teacher):
        id_address = self._create_address(new_teacher)
        new_teacher.address = id_address
        id_person = self._create_person(new_teacher)

        insert = f"INSERT INTO teachers (id_person, languages, " \
            f"courses_id, diplomas, salary) " \
            f"VALUES ('{id_person}', '{new_teacher.languages}', " \
            f"'{new_teacher.courses_id}', '{new_teacher.diplomas}', '{new_teacher.salary}')"
        self.cursor.execute(insert)
        self._set_id()
        self.connection.commit()

    def find_by_id(self, id_teacher):
        self.cursor.execute("SELECT PERSONS.ID_PERSON, PERSONS.NAME, PERSONS.SURNAME, "
                            "PERSONS.EMAIL, PERSONS.PHONE, PERSONS.id_address, "
                            "TEACHERS.id_teacher, TEACHERS.languages, TEACHERS.courses_id,"
                            "TEACHERS.diplomas, TEACHERS.salary FROM PERSONS "
                            "INNER JOIN TEACHERS ON PERSONS.id_person = TEACHERS.id_person "
                            "WHERE TEACHERS.id_teacher=?", (id_teacher,))
        result = self.cursor.fetchone()
        addr_mapper = AddressMapper(self.connection)
        address = addr_mapper.find_by_id(result[5])
        person_factory = PersonFactory()
        teacher = person_factory.create_person('teacher', *result[:5],
                                               address=address, id_teacher=result[6],
                                               languages=result[7], courses_id=result[8],
                                               diplomas=result[9], salary=result[10])
        if teacher:
            return teacher
        else:
            raise RecordNotFoundException(f'record with id={id} not found')

    def _set_id(self):
        self.cursor.execute('SELECT last_insert_rowid();')
        self.id_teacher = self.cursor.fetchone()[0]

    def update(self, updated_teacher):
        addr = updated_teacher.address
        self.addr_mapper.update(addr)
        self.person_mapper.update(updated_teacher)
        update_script = f"UPDATE TEACHERS SET languages=?, courses_id=?, " \
            f"diplomas=?, salary=? WHERE id_teacher=?"
        self.cursor.execute(update_script, (updated_teacher.languages, updated_teacher.courses_id,
                                            updated_teacher.diplomas, updated_teacher.salary,
                                            updated_teacher.id_teacher))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        delete_script = f"DELETE FROM TEACHERS WHERE id_teacher = ?"
        self.cursor.execute(delete_script, (obj.id_teacher,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)

    def count(self):
        count_script = f"SELECT count(*) FROM TEACHERS"
        self.cursor.execute(count_script)
        result = self.cursor.fetchone()[0]
        return result
