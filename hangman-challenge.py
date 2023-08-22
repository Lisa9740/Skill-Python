# bonus make the program take the input from the user and make it lowercase
import random

# create a word list
words = ['water', "house", "kitchen", "flower", "theatre"]


# check if the letter is in the word
def check_letter_in_the_word(letter, word):
    if letter in word:
        found_letter = ""
        count_letter = word.count(letter)
        for i in range(count_letter):
            found_letter += letter
        return letter
    else:
        return ""


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


def is_a_winning_game(letters, word, chances):
    is_win = False
    is_end = False
    if len(letters) == len(word):
        is_win = True
        is_end = True
        print(f"\nCongratulation the word was {word} !")
    status_play_message(True, is_end, is_win, chances)


def is_game_over(chances):
    if chances < 1:
        status_play_message(False, True, False, chances)
    else:
        status_play_message(False, False, False, chances)


def check_if_already_found(letter, letters):
    if letter in letters:
        return True
    else:
        return False


# ask a user to guess a letter
def play(word_list):
    # randomly choose a word from the list
    word = random.choice(word_list)
    letters_guessed = ""
    chances = 8
    chances_left = chances

    print(f"Let's begin ! Guess the word, you have {chances} chances : ")

    while chances_left > 0:
        letter = input("Guess a letter of the word : ")
        letter_guessed = check_letter_in_the_word(letter, word)

        if letter_guessed != "":
            if check_if_already_found(letter, letters_guessed) is False:
                letters_guessed += letter_guessed.lower()
                is_a_winning_game(letters_guessed, word, chances_left)
            else:
                print("You have already entered this letter. Retry!")
                continue
        else:
            chances_left -= 1
            is_game_over(chances_left)


play(words)

# create a greeting
print("------------  Thank you for using this program -----------------")
