#!/usr/bin/python3
from .file_storage import FileStorage
from .ipersistence_manager import IPersistenceManager


class DataManager(IPersistenceManager):
    def __init__(self, storage: FileStorage):
        self.storage = storage

    def save(self, entity):
        self.storage.save(entity)

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_id, entity_type)

    def update(self, entity):
        self.storage.update(entity)

    def delete(self, entity_id, entity_type):
        self.storage.delete(entity_id, entity_type)
