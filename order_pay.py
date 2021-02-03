import abc


class Payment(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def pay(self, order_number, amount):
        pass


class PayPalPayment(Payment):

    def __init__(self, email, token):
        self.email = email
        self.token = token

    def pay(self, order_number, amount):
        return f'Payment order {order_number} by PayPal ' \
            f'in the {amount} made'


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

    def pay(self, order_number, amount):
        return f'Payment {order_number} by Credit Card ' \
            f'in the {amount} made'


class GiftCertificate:

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number


class GiftCertificatePayment(Payment):

    def __init__(self, certificate):
        self.certificate = certificate

    def pay(self, order_number, amount):
        return f'Payment {order_number} by Gift Certificate ' \
            f'in the {amount} made'


class Order:

    """Pattern Strategy"""

    number = 0

    def __init__(self, customer):
        Order.number += 1
        self.order_number = Order.number
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_order_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

    def pay(self, payment):
        total_price = self.get_order_price()
        return payment.pay(self.order_number, total_price)
