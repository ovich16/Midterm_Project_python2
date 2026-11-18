from menu import welcome_message
from fake_game_move import fake_move
from choose_word import get_word

def main():
    diff_choice = welcome_message()

    guesses_made = []
    for i in range(diff_choice):
        guesses_made = fake_move(guesses_made)

    word = get_word(guesses_made)
    print(word)

if __name__ == '__main__':
    main()