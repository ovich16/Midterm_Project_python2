from menu import welcome_message
from fake_game_move import fake_move
from choose_word import get_word
from game_move import move
from end import end_game

def main():
    while True:
        diff_choice = welcome_message()

        wrong_guesses_made = []
        for i in range(diff_choice):
            wrong_guesses_made = fake_move(wrong_guesses_made)

        word = get_word(wrong_guesses_made)

        guess = '         '
        while True:
            move_result = move(word, guess, wrong_guesses_made)
            if move_result == (False, False):
                break
            else:
                guess = move_result[0]
                wrong_guesses_made = move_result[1]

        ending = end_game(guess, wrong_guesses_made, word)
        if ending == True:
            break

if __name__ == '__main__':
    main()