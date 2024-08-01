import random
from enum import IntEnum

class Action(IntEnum):
    Windows = 0
    Mac = 1
    Linux = 2
    
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
    if user_action == computer_action:
        print (f"\nBoth players have selected {user_action.name}! It is a tie!\n")
    elif user_action == Action.Windows:
        if computer_action == Action.Linux:
            print("\nWindows wounds Linux! You win!\n")
        else:
            print("\nMac breaks Windows! You lose!\n")
    elif user_action == Action.Mac:
        if computer_action == Action.Windows:
            print("\nMac breaks Windows! You win!\n")
        else:
            print("\nLinux eats Mac. You lose!\n")
    elif user_action == Action.Linux:
        if computer_action == Action.Mac:
            print("\nLinux eats Mac. You win!\n")
        else:
            print("\nWindows wounds Linux. You lose!\n")

print("The battle of the Operating System is here!\n"
      + "\nRules of the game:\n"
      + "Windows vs Mac -> Mac wins.\n"
      + "Mac vs Linux -> Linux wins.\n"
      + "Linux vs Windows -> Windows wins.\n")

while True:
    try:
        user_action = get_user_selection()
        print(f"You chose {user_action}")
    except ValueError as e:
        range_str = f"[0, {len(Action) -1}]"
        print(f"\nInvalid selection. Enter a value in range {range_str}\n")
        continue

    computer_action = get_computer_selection()
    print(f"The computer selected {computer_action}")
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n)? ")
    if play_again.lower() != "y":
        break