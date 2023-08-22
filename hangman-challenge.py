# bonus make the program take the input from the user and make it lowercase
import random
import re

# create a word list
words = ['water', "house", "kitchen", "flower", "theatre"]
word_chosen = random.choice(words)


# displays word to a secret format to player
def set_secret_word_display(word):
    word_to_guess = []
    for i in word:
        word_to_guess.append("-")
    return word_to_guess


# search in word occurrence(s) of a guesses letter
def check_guess(letter, word, secret_word):
    indexes = [m.start() for m in re.finditer(letter, word)]
    for i in indexes:
        secret_word[i] = letter
    return secret_word


def set_player_point(chances_left):
    return chances_left * 4


def right_guess(chances):
    if chances > 0:
        print(f"Cool you guess right!")


def winning_game(secret_word, chances):
    print(f"\nCongratulation the word was {''.join(secret_word)} ! \n"
          f"You win ! You have {set_player_point(chances)} points !")


def wrong_guess(chances):
    if chances >= 1:
        print(f"Retry !")
    else:
        print("Game Over !")


# ask a user to guess a letter
def play():
    # randomly choose a word from the list
    secret_word = set_secret_word_display(word_chosen)
    chances_left = 8
    print(f"Let's begin ! Guess the word, you have {chances_left} chances : "
          f"\n{' , '.join(secret_word)} ")

    while chances_left > 0:
        guess = input("Guess a letter of the word : ")
        # check if player's guess not empty
        if len(guess.strip()) == 0: continue

        word_to_guess = check_guess(guess, word_chosen, secret_word)
        display_word = " , ".join(word_to_guess)

        print(f" {display_word}  |  You have {chances_left} chances left")

        if guess in word_to_guess:
            if not "-" in display_word:
                winning_game(word_to_guess, chances_left)
                break
            right_guess(chances_left)
        else:
            chances_left -= 1
            wrong_guess(chances_left)


play()

# create a greeting
print("------------  Thank you for using this program -----------------")
