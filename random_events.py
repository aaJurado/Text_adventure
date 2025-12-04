import random

def random_event(player):
    """
    Random events that may occur when the player moves.
    Returns a message string or None.
    """
    roll = random.randint(1, 4)

    if roll == 1:
        player.health -= 10
        return "A hidden trap snaps! You lose 10 health."

    elif roll == 2:
        player.health += 10
        return "You find a healing fountain. You gain 10 health."

    # No event this time
    return None
