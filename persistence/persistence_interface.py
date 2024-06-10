from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        """save entity to database"""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """get entity from database"""
        pass

    @abstractmethod
    def update(self, entity):
        """update entity in database"""
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """delete entity from database"""
        pass
