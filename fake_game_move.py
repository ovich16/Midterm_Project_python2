import hangman

def fake_move(guesses_made):
    unsuccessful_tries = len(guesses_made)

    print(f"""\033[2J\033[H", end=\n
{' '*19}😈😈😈 TRY TO GUESS THE WORD I AM THINKING OF! 😈😈😈
{'='*90}
Enter a letter that you think is in the word below.
{'='*90}\n
{' '*35 + '_ '*9}\n
{'='*90}""")
    hangman_options = {0:hangman.hangman0,
                       1:hangman.hangman1,
                       2:hangman.hangman2,
                       3:hangman.hangman3}
    hangman_options[unsuccessful_tries]()
    print('='*90)
    user_move = input('\nYOUR GUESS: ').lower()
    guesses_made.append(user_move)

fake_move(['f'])