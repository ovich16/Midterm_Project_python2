from menu import welcome_message
from fake_game_move import fake_move

diff_choice = welcome_message()

excluded_letters = []
for i in range(diff_choice):
    excluded_letters = fake_move(excluded_letters)