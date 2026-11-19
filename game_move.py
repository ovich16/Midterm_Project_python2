import hangman

def move(word, guess, wrong_guesses_made):
    word_to_print = ''
    letters_guessed = 0
    unsuccessful_tries = len(wrong_guesses_made)

    for letter in guess:
        if letter == ' ':
            word_to_print = word_to_print + '_' + ' '
        else:
            word_to_print = word_to_print + letter.upper() + ' '
            letters_guessed +=1

    print(f"""\033[2J\033[H", end=\n
{' '*19}😈😈😈 TRY TO GUESS THE WORD I AM THINKING OF! 😈😈😈
{'='*90}
Enter a letter that you think is in the word below.
{'='*90}\n
{' '*35 + word_to_print}\n
{'='*90}""")

    hangman_options = {1:hangman.hangman1,
                       2:hangman.hangman2,
                       3:hangman.hangman3,
                       4:hangman.hangman4,
                       5:hangman.hangman5,
                       6:hangman.hangman6,
                       7:hangman.hangman7,
                       8:hangman.hangman8,
                       9:hangman.hangman9}
    hangman_options[unsuccessful_tries]()
    print('='*90)
    user_move = input('\nYOUR GUESS: ').lower()

move('consensus', '         ', ['a','i','m'])