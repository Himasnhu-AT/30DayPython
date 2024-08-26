
# Day 27 code implementation in Python

# Game state
game_running = True
location = "entrance of a dark forest"

# Game loop
while game_running:
    print(f"You are standing at the {location}.")
    print("Press 'f' to move forward or 'q' to quit")

    action = input("What do you want to do? ")

    if action == 'f':
        location = "a clearing"
        print("You venture deeper into the forest and reach a clearing.")
    elif action == 'q':
        game_running = False
        print("You decide to leave the forest.")
    else:
        print("Invalid action. Please try again.")

