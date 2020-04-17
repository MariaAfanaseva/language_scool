from sqlite_db.mappers.unit_of_work import UnitOfWork
from sqlite_db.mappers.get_mapper import MapperRegistry
from persons import PersonFactory
from address import AddressBuilder


class UpdateDatabase:
    def __init__(self, connection):
        self.connection = connection

    def save_teacher(self, name, surname, email, phone,
                     country, city, languages,
                     courses_id, diplomas):
        UnitOfWork.new_current()
        update = UnitOfWork.get_current()
        update.set_mapper_registry(MapperRegistry(self.connection))

        address = AddressBuilder().set_country(country). \
            set_city(city).build()
        person_factory = PersonFactory()
        teacher = person_factory.create_person(
            'teacher', None, name=name, surname=surname,
            email=email, phone=phone, address=address,
            languages=languages, diplomas=diplomas,
            courses_id=courses_id, id_teacher=None)
        teacher.mark_new()
        UnitOfWork.get_current().commit()
