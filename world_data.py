from models import Room, Item

# ----------------- ITEMS -----------------

potion = Item(
    name="potion",
    description="A glowing potion that restores 25 health.",
    usable=True,
    effect="heal",
)

key = Item(
    name="key",
    description="A small rusty key. It looks important.",
    usable=True,
    effect="unlock",
)

torch = Item(
    name="torch",
    description="A wooden torch that can light dark places.",
    usable=False,
)

# ----------------- ROOMS -----------------

rooms = {
    "Village": Room(
        name="Village",
        description="A peaceful village with stone paths and wooden houses.",
        exits={"north": "Forest"},
        items=[potion],
    ),
    "Forest": Room(
        name="Forest",
        description="A dense forest. The trees block most of the light.",
        exits={"south": "Village", "east": "Cave"},
        items=[torch],
    ),
    "Cave": Room(
        name="Cave",
        description="A dark, cold cave. You hear dripping water.",
        exits={"west": "Forest"},
        items=[key],
    ),
}