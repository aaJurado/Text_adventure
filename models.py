class Item:
    """
    Represents an item that can be picked up, stored, or used.
    """
    def __init__(self, name, description, usable=False, effect=None):
        self.name = name.lower()
        self.description = description
        self.usable = usable
        self.effect = effect

    def __str__(self):
        return f"{self.name}: {self.description}"


class Room:
    """
    Represents a room in the game world.
    """
    def __init__(self, name, description, exits, items=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items or []

    def __str__(self):
        return self.name


class Player:
    """
    Represents the player and their stats.
    """
    def __init__(self, start_location):
        self.location = start_location
        self.inventory = []
        self.health = 100

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item_name):
        self.inventory = [i for i in self.inventory if i.name != item_name]

    def has_item(self, item_name):
        return any(i.name == item_name.lower() for i in self.inventory)
