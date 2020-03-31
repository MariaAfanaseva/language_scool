import abc


class Payment(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def pay(self, amount):
        pass


class PayPalPayment(Payment):

    def __init__(self, email, token):
        self.email = email
        self.token = token

    def pay(self, amount):
        return f'Payment bei PayPal in the {amount} made'


class CreditCard:

    def __init__(self, number, owner_name, code):
        self._number = number
        self._owner_name = owner_name
        self._code = code

    def get_number(self):
        return self._number


class CreditCardPayment(Payment):

    def __init__(self, card):
        self.card = card

    def pay(self, amount):
        return f'Payment bei Credit Card in the {amount} made'


class GiftCertificate:

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number


class GiftCertificatePayment(Payment):

    def __init__(self, certificate):
        self.certificate = certificate

    def pay(self, amount):
        return f'Payment bei Gift Certificate in the {amount} made'


class Order:

    """Pattern Strategy"""

    def __init__(self):
        self._items = []

    def add_course(self, item):
        self._items.append(item)

    def get_order_price(self):
        total_price = 0
        for item in self._items:
            total_price += item.price
        return total_price

    def pay(self, payment):
        total_price = self.get_order_price()
        payment.pay(total_price)
