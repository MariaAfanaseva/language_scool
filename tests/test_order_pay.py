import unittest
from persons import PersonFactory
from course import CreateCourse
from address import AddressBuilder
from order_pay import (Order, CreditCard, CreditCardPayment,
                       PayPalPayment, GiftCertificate,
                       GiftCertificatePayment)


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.address = AddressBuilder().set_city('Rom').build()
        self.course_1 = CreateCourse().set_price(500).build()
        self.course_2 = CreateCourse().set_price(400).build()
        self.customer = PersonFactory.create_person('student', 1, 'Mama',
                                                    'Li', 'mama@h', '9009', self.address,
                                                    id_student=1, language_level=['Italian A2', 'English B2'],
                                                    courses_id=[56])
        self.order = Order(self.customer)
        self.number = self.order.order_number
        self.order.add_item(self.course_1)
        self.order.add_item(self.course_2)

    def test_init(self):
        self.assertEqual(self.order.order_number, self.number)
        self.assertIsInstance(self.order.items, list)

    def test_add_item(self):
        self.assertIn(self.course_1, self.order.items)
        self.assertEqual(self.course_1.price, 500)

    def test_get_order_price(self):
        self.assertEqual(self.order.get_order_price(), 900)

    def test_pay(self):
        card = CreditCard(34459776554, 'Maria', 1587)
        payment_credit_card = CreditCardPayment(card)
        self.assertEqual(self.order.pay(payment_credit_card),
                         f'Payment {self.number} by Credit Card in the 900 made')
        payment_pay_pal = PayPalPayment('mari@ru', 'token')
        self.assertEqual(self.order.pay(payment_pay_pal),
                         f'Payment order {self.number} by PayPal in the 900 made')
        gift_certificate = GiftCertificate(555)
        payment_gift_certificate = GiftCertificatePayment(gift_certificate)
        self.assertEqual(self.order.pay(payment_gift_certificate),
                         f'Payment {self.number} by Gift Certificate in the 900 made')

    def tearDown(self):
        Order.number -= 1


if __name__ == '__main__':
    unittest.main()
