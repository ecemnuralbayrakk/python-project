import urllib.request
import random

def get_word():
    word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    words = long_txt.splitlines()
    return random.choice(words)

def letters(word, correct_guesses):
    display_word = []
    for letter in word:
        if letter in correct_guesses:
            display_word.append(letter)  
        else:
            display_word.append("_")  

    print(" ".join(display_word))

def guess(word):
    wrong_guesses = 0
    correct_guesses = set()
    all_guesses = set()

    while wrong_guesses < 6:
        letters(word, correct_guesses)
        guess = input("Guess a letter: ").lower()

        if guess in all_guesses:
            print("You already guessed that letter. Try again.")
            continue

        all_guesses.add(guess)

        if guess in word:
            print("Correct!")
            correct_guesses.add(guess)
        else:
            print("Incorrect!")
            wrong_guesses += 1

        if set(word) == correct_guesses:
            print("You win! The word was:", word)
            break

        print("You have {} wrong guesses left.".format(6 - wrong_guesses))
    
    if wrong_guesses == 6:
        print("You lose! The word was:", word)

def play_hangman(word):
    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))
    print("Press Enter to start guessing.")
    input() 
    guess(word)

def main():
    word = get_word()
    play_hangman(word)

if __name__ == "__main__":
    main()