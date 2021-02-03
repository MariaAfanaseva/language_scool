class Address:

    def __init__(self, id_address, country, region, city, street,
                 house_number, apartment_number, postcode):
        self.id_address: int = id_address
        self.country: str = country
        self.region: str = region
        self.city: str = city
        self.street: str = street
        self.house_number: str = house_number
        self.apartment_number: str = apartment_number
        self.postcode: str = postcode

    def __str__(self):
        ret = ''
        for value in self.__dict__.values():
            ret += f'{value},'
        return ret


class AddressBuilder:

    """ Pattern Builder """

    def __init__(self):
        self.address = Address(None, '', '', '', '', '', '', '')

    def set_id_address(self, id_address):
        self.address.id_address = id_address
        return self

    def set_country(self, country):
        self.address.country = country
        return self

    def set_region(self, region):
        self.address.region = region
        return self

    def set_city(self, city):
        self.address.city = city
        return self

    def set_street(self, street):
        self.address.street = street
        return self

    def set_house_number(self, house_number):
        self.address.house_number = house_number
        return self

    def set_apartment_number(self, apartment_number):
        self.address.apartment_number = apartment_number
        return self

    def set_postcode(self, postcode):
        self.address.postcode = postcode
        return self

    def build(self):
        return self.address
