import random

while True:
    print("The battle of the Operating System is here!\n"
        + "\nRules of the game:\n"
        + "Windows vs Mac -> Mac wins.\n"
        + "Mac vs Linux -> Linux wins.\n"
        + "Linux vs Windows -> Windows wins.\n")

    user_action = input ("Enter a choice (Windows, Mac, Linux): ")

    possible_actions = ["Windows","Mac","Linux"]
    computer_action = random.choice(possible_actions)

    print(f"\nYou chose {user_action} as your OS, the computer chose {computer_action} as OS.\n")

    if user_action == computer_action:
        print(f"You both chose {user_action}. It is a tie!")
    elif user_action == "Windows":
        if computer_action == "Linux":
            print ("Windows wounds Linux! You win!\n")
        else:
            print ("Mac breaks Windows! You lose!\n")
    elif user_action == "Mac":
        if computer_action == "Windows":
            print ("Mac breaks Windows! You win!\n")
        else:
            print ("Linux eats Mac! You lose!\n")
    elif user_action == "Linux":
        if computer_action == "Mac":
            print("Linux eats Mac! You win!\n")
        else:
            print("Windows wounds Linux! You lose!\n")

    play_again = input("Play again? (y/n)? ")
    if play_again.lower() != "y":
        break