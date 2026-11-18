from menu import welcome_message
from fake_game_move import fake_move

def main():
    diff_choice = welcome_message()

    guesses_made = []
    for i in range(diff_choice):
        guesses_made = fake_move(guesses_made)


if __name__ == '__main__':
    main()