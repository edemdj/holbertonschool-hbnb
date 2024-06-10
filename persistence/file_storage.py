#!/usr/bin/python3
import json
import os

class FileStorage:
    def __init__(self, file_path='data.json'):
        self.file_path = file_path

    def save(self, entity):
        data = self.load()
        entity_id = entity.user_id
        data[entity_id] = entity.to_dict()
        self.write(data)

    def get(self, entity_id, entity_type):
        data = self.load()
        entity_data = data.get(entity_id)
        if entity_data:
            return entity_type(**entity_data)
        return None

    def update(self, entity):
        self.save(entity)

    def delete(self, entity_id, entity_type):
        data = self.load()
        if entity_id in data:
            del data[entity_id]
            self.write(data)

    def load(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
