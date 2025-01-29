import random

def game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game!")
        print("-------------------------------")
        print(f"User Score: {user_score}")
        print(f"Computer Score: {computer_score}")
        print("-------------------------------")

        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        while user_choice not in ["rock", "paper", "scissors", "q"]:
            user_choice = input("Invalid input. Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

        if user_choice == "q":
            print("\nGame Over!")
            print(f"Final Score - User: {user_score}, Computer: {computer_score}")
            break

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        print(f"\nUser chose {user_choice}, computer chose {computer_choice}.\n")

        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! User wins this round!")
                user_score += 1
            else:
                print("Paper covers rock! Computer wins this round!")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! User wins this round!")
                user_score += 1
            else:
                print("Scissors cuts paper! Computer wins this round!")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! User wins this round!")
                user_score += 1
            else:
                print("Rock smashes scissors! Computer wins this round!")
                computer_score += 1

        play_again = input("Play another round? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Invalid input. Play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nGame Over!")
            print(f"Final Score - User: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    game()
