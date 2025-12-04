from models import Player
from game import take_item, use_item, go_direction


def test_take_item():
    player = Player(start_location="Village")
    msg = take_item(player, "potion")

    assert "take the potion" in msg.lower()
    assert any(item.name == "potion" for item in player.inventory)


def test_go_direction():
    player = Player(start_location="Village")
    msg = go_direction(player, "north")

    assert player.location == "Forest"
    assert "forest" in msg.lower()


def test_use_heal_item():
    player = Player(start_location="Village")
    take_item(player, "potion")
    old_health = player.health

    msg = use_item(player, "potion")

    assert player.health > old_health
    assert "feel better" in msg.lower()


if __name__ == "__main__":
    test_take_item()
    test_go_direction()
    test_use_heal_item()
    print("All tests passed!")
