
# Day 30 - Simple Text-Based Adventure Game (Sample Implementation)

import random

# Game data
locations = {
    "start": {
        "description": "You stand at the entrance to a dark forest. A path leads north.",
        "exits": {"north": "forest"}
    },
    "forest": {
        "description": "You are in a dense forest. The air is thick with the scent of pine needles.",
        "exits": {"south": "start", "east": "clearing"}
    },
    "clearing": {
        "description": "You reach a sun-drenched clearing. A small cottage sits on the edge.",
        "exits": {"west": "forest", "enter cottage": "cottage"}
    },
    "cottage": {
        "description": "Inside the cottage, an old woman sits by the fireplace. She looks up as you enter.",
        "exits": {"leave": "clearing"}
    }
}

player = {
    "location": "start",
    "inventory": []
}

def describe_location():
    """Prints the description of the player's current location."""
    location = locations[player["location"]]
    print(location["description"])
    print_exits(location)

def print_exits(location):
    """Prints the available exits from the current location."""
    if location["exits"]:
        print("You can go:")
        for direction, destination in location["exits"].items():
            print(f"{direction.title()} to {destination}")

def move(direction):
    """Handles player movement to a new location."""
    current_location = locations[player["location"]]
    if direction in current_location["exits"]:
        player["location"] = current_location["exits"][direction]
        describe_location()
    else:
        print("You can't go that way.")

def talk_to_woman():
    """Handles the interaction with the old woman."""
    print("Old Woman: Welcome, traveler. What brings you to my humble abode?")
    while True:
        response = input("What do you say? ").lower()
        if response == "hello" or response == "hi":
            print("Old Woman: Greetings! I am Elara. I've seen many travelers pass through here.")
            print("Old Woman: If you are in need of a safe haven, you are welcome to stay a while.")
        elif response == "leave" or response == "goodbye":
            print("Old Woman: Farewell then! May your journey be safe.")
            break
        else:
            print("Old Woman: I'm not sure I understand.")

def take_item(item):
    """Handles taking an item."""
    current_location = locations[player["location"]]
    if item in current_location:
        print(f"You take the {item}.")
        player["inventory"].append(item)
    else:
        print("There is no such item here.")

def inventory():
    """Prints the player's inventory."""
    if player["inventory"]:
        print("You are carrying:")
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

def game_loop():
    """The main game loop."""
    describe_location()
    while True:
        command = input("> ").lower()
        words = command.split()

        if words[0] == "go":
            if len(words) > 1:
                move(words[1])
            else:
                print("Go where?")
        elif words[0] == "talk" and words[1] == "to" and words[2] == "woman":
            talk_to_woman()
        elif words[0] == "take":
            if len(words) > 1:
                take_item(words[1])
            else:
                print("Take what?")
        elif words[0] == "inventory":
            inventory()
        elif words[0] == "quit":
            break
        else:
            print("Invalid command.")

# Start the game
print("Welcome to the Forest of Shadows!")
game_loop()
print("Thank you for playing!")

