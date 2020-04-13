import threading


class UpdateDatabase:

    """
    Pattern Unit of work
    """

    current = threading.local()

    def __init__(self):
        self.new_objects = []
        self.update_objects = []
        self.removed_objects = []
        self.mapper_registry = None

    def set_mapper_registry(self, mapper):
        self.mapper_registry = mapper

    def register_new(self, obj):
        self.new_objects.append(obj)

    def register_update(self, obj):
        self.update_objects.append(obj)

    def register_remove(self, obj):
        self.removed_objects.append(obj)

    def insert_data(self):
        for obj in self.new_objects:
            self.mapper_registry.get_mapper(obj).insert(obj)
            self.new_objects.clear()

    def update_data(self):
        for obj in self.update_objects:
            self.mapper_registry.get_mapper(obj).update(obj)
            self.update_objects.clear()

    def delete_data(self):
        for obj in self.removed_objects:
            self.mapper_registry.get_mapper(obj).delete(obj)
            self.removed_objects.clear()

    def commit(self):
        self.insert_data()
        self.update_data()
        self.delete_data()

    @staticmethod
    def new_current():
        __class__.set_current(UpdateDatabase())

    @classmethod
    def set_current(cls, update_db_class):
        cls.current.update_db_class = update_db_class

    @classmethod
    def get_current(cls):
        return cls.current.update_db_class


class UpdateDBObject:
    def mark_new(self):
        UpdateDatabase.get_current().register_new(self)

    def mark_update(self):
        UpdateDatabase.get_current().register_update(self)

    def mark_removed(self):
        UpdateDatabase.get_current().register_remove(self)
