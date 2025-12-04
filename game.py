from models import Item
from world_data import rooms
from random_events import random_event


# ---------------- ROOM DESCRIPTION ----------------

def describe_room(player):
    room = rooms[player.location]
    lines = [
        f"You are in the {room.name}.",
        room.description,
    ]

    # Exits
    exits_str = ", ".join(
        f"{direction} -> {dest}"
        for direction, dest in room.exits.items()
    )
    lines.append(f"Exits: {exits_str}")

    # Items
    if room.items:
        items_str = ", ".join(item.name for item in room.items)
        lines.append(f"You see: {items_str}")

    lines.append(f"Your health: {player.health}")

    return "\n".join(lines)


# ---------------- MOVEMENT ----------------

def go_direction(player, direction):
    direction = direction.lower()
    room = rooms[player.location]

    if direction not in room.exits:
        return "You cannot go that way."

    player.location = room.exits[direction]

    # Random event happens after moving
    event_msg = random_event(player)
    desc = describe_room(player)

    if event_msg:
        return event_msg + "\n" + desc
    else:
        return desc


# ---------------- LOOK ----------------

def look(player):
    return describe_room(player)


# ---------------- TAKE ITEM ----------------

def take_item(player, item_name):
    item_name = item_name.lower()
    room = rooms[player.location]

    for item in room.items:
        if item.name == item_name:
            room.items.remove(item)
            # Give the player a copy
            new_item = Item(item.name, item.description, item.usable, item.effect)
            player.add_item(new_item)
            return f"You take the {item_name}."
    return f"There is no {item_name} here."


# ---------------- DROP ITEM ----------------

def drop_item(player, item_name):
    item_name = item_name.lower()

    for item in player.inventory:
        if item.name == item_name:
            player.inventory.remove(item)
            rooms[player.location].items.append(item)
            return f"You drop the {item_name}."

    return f"You don't have a {item_name}."


# ---------------- INVENTORY ----------------

def show_inventory(player):
    if not player.inventory:
        return "Your inventory is empty."

    lines = ["You are carrying:"]
    for item in player.inventory:
        lines.append(f"- {item.name}: {item.description}")
    return "\n".join(lines)


# ---------------- USE ITEM ----------------

def use_item(player, item_name):
    item_name = item_name.lower()

    for item in player.inventory:
        if item.name == item_name:

            if not item.usable:
                return f"You cannot use the {item_name}."

            # Healing potion
            if item.effect == "heal":
                player.health += 25
                player.inventory.remove(item)
                return "You drink the potion and feel better (+25 health)."

            # Unlock event (Cave treasure)
            if item.effect == "unlock" and player.location == "Cave":
                return (
                    "You unlock a hidden stone door in the cave.\n"
                    "Inside is ancient treasure.\n"
                    "✨ YOU WIN THE GAME! ✨"
                )

            return f"You use the {item_name}, but nothing happens."

    return f"You don't have a {item_name}."


# ---------------- HELP ----------------

def help_text():
    return (
        "Commands:\n"
        "  look              - describe the room\n"
        "  go <direction>    - move north/south/east/west\n"
        "  take <item>       - pick up an item\n"
        "  drop <item>       - drop an item\n"
        "  use <item>        - use an item\n"
        "  inventory         - list items you're carrying\n"
        "  save              - save the game\n"
        "  load              - load the game\n"
        "  help              - show this help\n"
        "  quit              - exit the game"
    )


# ---------------- COMMAND HANDLER ----------------

def handle_command(player, command):
    if not command:
        return "Please enter a command."

    parts = command.strip().split()
    verb = parts[0].lower()

    if verb == "look":
        return look(player)

    elif verb == "go":
        if len(parts) < 2:
            return "Go where?"
        return go_direction(player, parts[1])

    elif verb == "take":
        if len(parts) < 2:
            return "Take what?"
        return take_item(player, parts[1])

    elif verb == "drop":
        if len(parts) < 2:
            return "Drop what?"
        return drop_item(player, parts[1])

    elif verb == "inventory":
        return show_inventory(player)

    elif verb == "use":
        if len(parts) < 2:
            return "Use what?"
        return use_item(player, parts[1])

    elif verb == "help":
        return help_text()

    # 'save' and 'load' are handled in main.py
    else:
        return "I don't understand that command. Type 'help' for commands."
