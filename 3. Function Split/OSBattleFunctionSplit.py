import random
from enum import IntEnum

class Action(IntEnum):
    Windows = 0
    Mac = 1
    Linux = 2

victories = {
    Action.Windows: [Action.Linux],
    Action.Mac: [Action.Windows],
    Action.Linux: [Action.Mac]
}
    
def get_user_selection():
    choices = [f"{action.name}[{action.value}] " for action in Action]
    choices_str = " - ".join(choices)
    selection = int(input (f"\nPick your OS ( {choices_str}): "))
    action = Action(selection)
    return action

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print (f"\nBoth players have selected {user_action.name}! It is a tie!\n")
    elif computer_action in defeats:
        print (f"\n{user_action.name} beats {computer_action.name}! You win!\n")
    else:
        print(f"\n{computer_action.name} beats {user_action.name}! You lose!\n")

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) -1}]"
        print(f"\nInvalid selection. Enter a value in range {range_str}\n")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("\nPlay again? (y/n)? ")
    if play_again.lower() != "y":
        break