import json

class Inventory:
    MAX_SIZE = 6

    def __init__(self):
        self.items = []

    def add(self, item_id):
        if len(self.items) >= self.MAX_SIZE:
            return False
        self.items.append(item_id)
        return True

    def remove(self, item_id):
        if item_id in self.items:
            self.items.remove(item_id)
            return True
        return False

    def has(self, item_id):
        return item_id in self.items

    def count(self):
        return len(self.items)

    def save(self):
        return self.items.copy()

    def load(self, data):
        self.items = data.copy()

    @staticmethod
    def load_definitions():
        with open("data/items.json") as f:
            return json.load(f)
