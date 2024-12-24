import random

import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def score(user_cards, computer_cards):
    if sum(user_cards) == sum(computer_cards):
        print("It's a draw")
        print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")
        return
    if sum(computer_cards) > 21:
        print("Computer went over. You win!")
        print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")
        return
    if sum(user_cards) > 21:
        print("You went over. You lose")
        print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")
        return
    if sum(computer_cards) > sum(user_cards):
        print("You lose")
        print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")

    elif sum(user_cards) > sum(computer_cards):
        print("You win!")
        print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's cards: {computer_cards}, final score: {sum(computer_cards)}")


def calculate_score(user_cards, computer_cards):
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    answer = input("Type 'y' to get another card, type 'n' to pass:")
    if answer == "y":
        user_cards.append(cards[random.randint(0, 12)])
        calculate_score(user_cards, computer_cards)
    while sum(computer_cards) < 17:
        computer_cards.append(cards[random.randint(0, 12)])

    score(user_cards, computer_cards)


def play(answer):
    while answer != "n":
        computer_cards = []
        user_cards = []
        if answer == "y":
            print(art.logo)
            user_cards.append(cards[random.randint(0, 12)])
            user_cards.append(cards[random.randint(0, 12)])
            computer_cards.append(cards[random.randint(0, 12)])
            calculate_score(user_cards, computer_cards)
            answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == "n":
        print("Goodbye")
        exit()


answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play(answer)
