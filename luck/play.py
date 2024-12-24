import random

from art import logo


def random_number():
    return random.randint(1, 100)


def return_prompt(number, predict):
    if number > predict:
        print(f"{predict} is too high.{number}")
        return "Too high."
    if number < predict:
        print(f"{predict} is too low.{number}")
        return "Too low."
    return f"You got it! The answer was {number}"


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number = random_number()
    print(number)

    if difficulty == "easy":
        for _ in range(10):
            print(f"You have {10 - _} attempts remaining to guess the number.")
            predict = int(input("Make a guess: "))
            print(return_prompt(number, predict))
            if number == predict:
                break
    else:
        for _ in range(5):
            print(f"You have {5 - _} attempts remaining to guess the number.")
            predict = int(input("Make a guess: "))
            print(return_prompt(number, predict))
            if number == predict:
                break


play_game()
