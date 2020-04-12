import sqlite3
from classes import AddressBuilder, PersonFactory
from sqlite_db.mappers.address_mapper import AddressMapper


class PersonMapper:

    """Pattern data mapper"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.id_person = None

    def insert(self, person):
        new_person = f"INSERT INTO PERSONS (name, surname, email, phone, id_address) " \
            f"VALUES ('{person.name}', '{person.surname}', " \
            f"'{person.email}', '{person.phone}', '{person.address}')"
        self.cursor.execute(new_person)
        self._set_ip()
        self.connection.commit()

    def _set_ip(self):
        self.cursor.execute('SELECT last_insert_rowid();')
        self.id_person = self.cursor.fetchone()[0]

    def update(self, updated_person):
        update_script = f"UPDATE PERSONS SET name=?, surname=?, " \
            f"email=?, phone=?, id_address=? WHERE id_person=?"
        self.cursor.execute(update_script, (updated_person.name, updated_person.surname,
                                            updated_person.email, updated_person.phone,
                                            updated_person.address.id_address, updated_person.id_person))
        self.connection.commit()


if __name__ == '__main__':
    connect = sqlite3.connect('school_db.sqlite')
    address = AddressBuilder().set_city('Berlin').set_street('Lenina').build()
    addr_mapper = AddressMapper(connect)
    addr_mapper.insert(address)
    id_address = addr_mapper.id_address

    person_factory = PersonFactory()
    person = person_factory.create_person(
                'teacher', 5, 'Nana',
                'Li',  'nana@mail.ru', 9009, id_address,
                id_teacher=2, salary=2000,
                languages=['Italian', 'English'],
                courses_id=[12],
                diplomas=['Ranish diploma']
            )
    mapper = PersonMapper(connect)
    mapper.insert(person)
    print(mapper.id_person)
