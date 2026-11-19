from menu import welcome_message
from fake_game_move import fake_move
from choose_word import get_word
from game_move import move

def main():
    diff_choice = welcome_message()

    guesses_made = []
    for i in range(diff_choice):
        guesses_made = fake_move(guesses_made)

    word = get_word(guesses_made)

    guess = '         '
    while True:
        end = move(word, guess, guesses_made)
        if end == True:
            break

if __name__ == '__main__':
    main()