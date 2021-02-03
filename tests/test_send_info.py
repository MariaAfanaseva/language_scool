import unittest
from collections import deque
from send_info import (CreateNotifier, EmailNotifier, SMSNotifier)


class TestCreateNotifier(unittest.TestCase):

    def setUp(self):
        self.email_notifier = CreateNotifier.get_notifier('EMAIL', 'school@ru')
        self.sms_notifier = CreateNotifier.get_notifier('SMS', '900')

    def test_get_notifier(self):
        self.assertIsInstance(self.email_notifier, EmailNotifier)
        self.assertEqual(self.email_notifier.sender_email, 'school@ru')
        self.assertIsInstance(self.sms_notifier, SMSNotifier)
        self.assertEqual(self.sms_notifier.sender_number, '900')


class TestEmailNotifier(unittest.TestCase):

    def setUp(self):
        self.email_notifier = CreateNotifier.get_notifier('EMAIL', 'school@ru')

    def test_init(self):
        self.assertEqual(self.email_notifier.sender_email, 'school@ru')

    def test_log(self):
        self.email_notifier.notify('test@test', 'Subject Test',
                                   'Text Test')
        data = ''
        with open(self.email_notifier._file_name, 'r') as file:
            for row in deque(file, 3):
                data += row.strip()
        text = 'connect: Login in school@ru,' \
               'send: Send to test@test from school@ru, ' \
               'subject Subject Test, message Text Test,' \
               'disconnect: Exit school@ru'
        self.assertEqual(data, text)


if __name__ == '__main__':
    unittest.main()
