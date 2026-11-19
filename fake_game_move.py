import hangman, re

def msg1():
    print(f"""\033[2J\033[H", end=\n
{' '*19}😈😈😈 TRY TO GUESS THE WORD I AM THINKING OF! 😈😈😈
{'='*90}\n
Enter a letter that you think is in the word below.\n
{'='*90}\n
{' '*35 + '_ '*9}\n
{'='*90}\n""")

def msg2():
    print(f"""\n{'='*90}
{' '*27}😈😈😈 YOUR GUESS IS WRONG! 😈😈😈
press ENTER to try again.
{'='*90}""")

def msg3():
    print(f"""\n{'='*90}
{' '*23}😈😈😈 YOU'VE ALREADY TRIED THIS LETTER! 😈😈😈
press ENTER to try again.
{'='*90}""")

def msg4():
    print(f"""\n{'='*90}
{' '*17}This value cannot be entered! Press ENTER to try again.""")


def fake_move(guesses_made):
    unsuccessful_tries = len(guesses_made)
    hangman_options = {0:hangman.hangman0,
                       1:hangman.hangman1,
                       2:hangman.hangman2}

    while True:
        msg1()
        hangman_options[unsuccessful_tries]()
        print('\n' + '='*90)
        user_move = input('\nYOUR GUESS: ').lower()
        if re.fullmatch(r'[a-z]', user_move) and user_move not in guesses_made:
            guesses_made.append(user_move)
            msg2()
            input()
            break
        elif user_move in guesses_made:
            msg3()
            input()
        else:
            msg4()
            input()
    return guesses_made