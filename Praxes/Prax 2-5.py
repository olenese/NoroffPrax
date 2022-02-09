from random import seed
from random import randint


def guessinggame():
    guess_another = "y"
    seed(1)

    while guess_another == "y":
        user_input = int(input("Please enter a value between 1 and 9: "))
        random_number = randint(0, 10)

        if user_input == random_number:
            print("Congratulations, you guessed correctly!")
        else: 
            print("Sorry, this was wrong. The correct number was: ", random_number)

        guess_another = input("Do you want to try again? If so, please enter y. Any other key ends the game. ")

if __name__ == "__main__":
    guessinggame()
