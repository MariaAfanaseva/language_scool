import sqlite3
from classes import AddressBuilder


class AddressMapper:

    """Pattern data mapper"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.id_address = None
        self.address_hash = {}

    def insert(self, address):
        new_person = f"INSERT INTO addresses (country, region, city, street, " \
            f"house_number, apartment_number, postcode) " \
            f"VALUES ('{address.country}', '{address.region}', " \
            f"'{address.city}', '{address.street}', '{address.house_number}', " \
            f"'{address.apartment_number}', '{address.postcode}')"
        self.cursor.execute(new_person)
        self._set_ip()
        self.connection.commit()

    def _set_ip(self):
        self.cursor.execute('SELECT last_insert_rowid();')
        self.id_address = self.cursor.fetchone()[0]

    def update(self, address):
        update_address = f"UPDATE ADDRESSES SET country=?, region=?, " \
            f"city=?, street=?, house_number=?, apartment_number=?, " \
            f"postcode=? WHERE id_address=?"
        self.cursor.execute(update_address, (address.country, address.region,
                                             address.city, address.street, address.house_number,
                                             address.apartment_number, address.postcode,
                                             address.id_address))

        self.connection.commit()


if __name__ == '__main__':
    address = AddressBuilder().set_city('Moscow').build()
    mapper = AddressMapper(sqlite3.connect('school_db.sqlite'))
    mapper.insert(address)
    print(mapper.id_address)
