import abc
from send_info import CreateNotifier


class Subject:
    """
    Pattern observer
    """

    def __init__(self):
        self._observers = set()
        self._phone = None
        self._email = None
        self._data = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.send(self, self._phone, self._email,
                          self._data)


class Observer(metaclass=abc.ABCMeta):

    def __init__(self):
        self._subject = None
        self._observer_state = None
        self._communication_type = None

    @abc.abstractmethod
    def send(self, arg):
        pass


class Message(Subject):

    @property
    def data(self):
        return self._phone, self._email, self._data

    @data.setter
    def data(self, data):
        # magical antipattern data[0], data[1], data[2]
        self._phone, self._email, self._data = data
        self._notify()


class NewsMessage(Message):

    def __init__(self, subject, message):
        super().__init__()
        self.subject = subject
        self.message = message


class PayMessage(Message):

    def __init__(self, subject, message):
        super().__init__()
        self.subject = subject
        self.message = message


class EmailMessage(Observer):

    def __init__(self, school_email):
        super().__init__()
        self._communication_type = 'EMAIL'
        self.notifier = CreateNotifier.get_notifier(self._communication_type,
                                                    school_email)

    def send(self, obj, phone, email, data):
        if isinstance(obj, PayMessage) and email:
            self.notifier.notify(email, obj.subject, f'{obj.message} {data}')
        if isinstance(obj, NewsMessage):
            self.notifier.notify(email, obj.subject, f'{obj.message} {data}')


class SMSMessage(Observer):

    def __init__(self, school_phone):
        super().__init__()
        self._communication_type = 'EMAIL'
        self.notifier = CreateNotifier.get_notifier(self._communication_type,
                                                    school_phone)

    def send(self, obj, phone, email, data):
        if isinstance(obj, PayMessage) and phone:
            self.notifier.notify(phone,  obj.subject, f'{obj.message} {data}')
