import random
def guess_number():
    try:
        range_top = int(input("Please input a number ").strip())
        if range_top <= 0:
            print("Please enter a number greater than 0 ")
            return
    except ValueError:
        print("please enter a valid number ")
        return

    number = random.randint(0, range_top)
    guesses = 0

    while True:
        try:
            user_guess = int(input("Please guess the number "))
            guesses += 1
            if user_guess == number:
                print(f"Correct Guess!! You got it in {guesses} guesses")
                break
            elif user_guess < number:
                print("Guess a higher number ")
            else:
                print("Guess a lower number ")
        except ValueError:
            print("Invalid input ")
            continue

if __name__ == "__main__":
    guess_number()