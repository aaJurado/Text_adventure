from models import Player
from game import describe_room, handle_command
from save_manager import save_game, load_game


def main():
    print("Welcome to the Text Adventure!")
    print("Type 'help' to see a list of commands.")
    print("Type 'quit' to exit the game.\n")

    # Try to load a saved game; if none, start in Village
    player = load_game()
    if player:
        print("Saved game found. Resuming your adventure...\n")
    else:
        player = Player(start_location="Village")

    print(describe_room(player))

    # Main game loop
    while True:
        command = input("\n> ").strip()

        if command.lower() == "quit":
            print("Goodbye!")
            break

        elif command.lower() == "save":
            save_game(player)
            print("Game saved.")
            continue

        elif command.lower() == "load":
            loaded = load_game()
            if loaded:
                player = loaded
                print("Game loaded.")
                print(describe_room(player))
            else:
                print("No saved game found.")
            continue

        # All other commands go through the game engine
        response = handle_command(player, command)
        print(response)

        # Simple win condition check
        if "you win the game" in response.lower():
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()
