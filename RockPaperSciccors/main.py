import random
from constants import Q, ROCK, PAPER, SCISSORS

user_options = [ROCK, PAPER, SCISSORS, Q]
computer_options = [ROCK, PAPER, SCISSORS]

computer_wins = 0
user_wins = 0
ties = 0
def rpc():
    while True:
        global user_wins, computer_wins, ties

        user_input = input("What is your choice? ").lower()
        if user_input == Q:
            break
        elif user_input not in user_options:
            print("Invalid options")
            continue

        computer_input = random.choice(computer_options)
        print(f"Computer chose {computer_input}")

        if (user_input == PAPER and computer_input == ROCK) or \
        (user_input == SCISSORS and computer_input == PAPER) or \
        (user_input == ROCK and computer_input == SCISSORS):
            print("You Won :)")
            user_wins += 1
        elif user_input == computer_input:
            print("It's a tie :|")
            ties += 1
        else:
            print("Computer Won :(")
            computer_wins += 1

    print(f"You won {user_wins} times")
    print(f"Computer won {computer_wins} times")
    print(f"You had {ties} ties")


if __name__ == "__main__":
    rpc()