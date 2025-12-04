import json
import os

from models import Player, Item

# Path: Text_adventure/saves/savefile.json
SAVE_FILE = os.path.join(os.path.dirname(__file__), "saves", "savefile.json")


def save_game(player):
    """
    Save the player's current state (location, health, inventory) to a file.
    """
    data = {
        "location": player.location,
        "health": player.health,
        "inventory": [
            {
                "name": item.name,
                "description": item.description,
                "usable": item.usable,
                "effect": item.effect,
            }
            for item in player.inventory
        ],
    }

    os.makedirs(os.path.dirname(SAVE_FILE), exist_ok=True)

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)


def load_game():
    """
    Load a saved game from disk.
    Returns a Player object or None if there is no saved game.
    """
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    player = Player(start_location=data["location"])
    player.health = data.get("health", 100)

    for item_data in data.get("inventory", []):
        item = Item(
            name=item_data["name"],
            description=item_data["description"],
            usable=item_data["usable"],
            effect=item_data["effect"],
        )
        player.add_item(item)

    return player
