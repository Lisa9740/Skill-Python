# bonus make the program take the input from the user and make it lowercase
import random
import re

# create a word list
words = ['watere', "housee", "kitcheen", "flowere", "theatre"]

# check if the guess is in the word
def check_guess_in_the_word(guess, word):
    if guess in word:
        found_letter = ""
        count_letter = word.count(guess)
        for i in range(count_letter):
            found_letter += guess
        return guess
    else:
        return ""


# displays word to a secret format to player
def set_secret_word(word):
    word_to_guess = []
    for i in word:
        word_to_guess.append("-")
    return word_to_guess


# search in word occurrence(s) of a guesses letter
def display_letter_at_guess(letter, word, word_to_guess):
    indexes = [m.start() for m in re.finditer(letter, word)]
    for i in indexes:
        word_to_guess[i] = letter
    return word_to_guess


def set_player_point(chances_left):
    return chances_left * 4


def status_play_message(is_found, is_games_ended, win, chances):
    if win:
        print(f"You win ! You have {set_player_point(chances)} point !")
    elif is_found is True:
        print(f"Cool you guess right! \n Keep going you have {chances} chances left.")
    elif is_games_ended is False & is_found is False:
        print(f"Retry ! \n Keep going you have {chances} chances left.")
    elif is_games_ended is True:
        print("Game Over !")


def is_a_winning_game(secret_word, chances):
    is_win = False
    is_end = False
    if not "-" in secret_word:
        is_win = True
        is_end = True
        print(f"\nCongratulation the word was {''.join(secret_word)} !")
    status_play_message(True, is_end, is_win, chances)
    if is_win == True:
        return True
    else:
        return False


def is_game_over(chances):
    if chances < 1:
        status_play_message(False, True, False, chances)
    else:
        status_play_message(False, False, False, chances)


def check_if_already_guessed(letter, letters):
    if letter in letters:
        return True
    else:
        return False


# ask a user to guess a letter
def play(word_list):
    # randomly choose a word from the list
    word = random.choice(word_list)
    secret_word = set_secret_word(word)
    guesses = ""
    chances = 8

    chances_left = chances

    print(f"Let's begin ! Guess the word, you have {chances} chances : "
          f"\n{' , '.join(secret_word)} ")

    while chances_left > 0 :
        guess = input("Guess a letter of the word : ")
        letter_guessed = check_guess_in_the_word(guess, word)

        if letter_guessed:
            if check_if_already_guessed(guess, guesses) is False:
                guesses += letter_guessed.lower()

                word_to_guess = display_letter_at_guess(letter_guessed, word, secret_word)
                print(" , ".join(word_to_guess))

                if is_a_winning_game(secret_word, chances_left):
                    break
            else:
                print("You have already entered this letter. Retry!")
                continue
        else:
            print(" , ".join(secret_word))
            chances_left -= 1
            is_game_over(chances_left)


play(words)

# create a greeting
print("------------  Thank you for using this program -----------------")
