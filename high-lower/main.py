from random import randint
from game_data import data
from art import logo, vs


def random_choice():
    random_id = randint(0, len(data) - 1)
    return data[random_id]


def compare(first, second):
    if first["follower_count"] > second["follower_count"]:
        return "A"
    else:
        return "B"


def play():
    score = 0
    first = random_choice()
    while True:
        print(logo)
        print(
            f"Against A: {first['name']}, a {first['description']} from {first['country']}"
        )
        print(vs)
        second = random_choice()
        if first == second:
            second = random_choice()
        print(
            f"Against B: {second['name']}, a {second['description']} from {second['country']}"
        )
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == compare(first, second):
            score += 1
            print(f"You're right! Current score: {score}")
            if compare(first, second) == "B":
                first = second
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break


play()
