import abc


class Notifier(metaclass=abc.ABCMeta):

    """Pattern template method"""

    def __init__(self):
        self._file_name = 'log_notifier.log'
        self._connect_data = ''
        self._send_data = ''
        self._disconnect_data = ''

    @abc.abstractmethod
    def _connect(self):
        pass

    @abc.abstractmethod
    def _send(self, recipient, subject, message):
        pass

    @abc.abstractmethod
    def _disconnect(self):
        pass

    def notify(self, recipient, subject, message):
        self._connect_data = self._connect()
        self._send_data = self._send(recipient, subject, message)
        self._disconnect_data = self._disconnect()
        self._log(recipient, subject, message)

    def _log(self, recipient, subject, message):
        with open(self._file_name, 'a') as file:
            file.write(f'connect: {self._connect_data}, \n'
                       f'send: {self._send_data}, \n'
                       f'disconnect: {self._disconnect_data}\n')


class SMSNotifier(Notifier):

    def __init__(self, sender_number):
        super().__init__()
        self.sender_number = sender_number

    def _connect(self):
        return f'Connect with number {self.sender_number}'

    def _send(self, recipient, subject, message):
        return f'Send to {recipient} from {self.sender_number}, ' \
            f'subject {subject}, message {message}'

    def _disconnect(self):
        pass


class EmailNotifier(Notifier):

    def __init__(self, sender_email):
        self.sender_email = sender_email
        super().__init__()

    def _connect(self):
        return f'Login in {self.sender_email}'

    def _send(self, recipient, subject, message):
        return f'Send to {recipient} from {self.sender_email}, ' \
            f'subject {subject}, message {message}'

    def _disconnect(self):
        return f'Exit {self.sender_email}'


class CreateNotifier:

    types = {
        'SMS': SMSNotifier,
        'EMAIL': EmailNotifier
    }

    @staticmethod
    def get_notifier(communication_type, sender):
        _notifier = CreateNotifier.types[communication_type]
        return _notifier(sender)
