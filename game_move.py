import hangman, message, check_end, re

def move(word, guess, wrong_guesses_made):
    hangman_options = {1:hangman.hangman1,
                           2:hangman.hangman2,
                           3:hangman.hangman3,
                           4:hangman.hangman4,
                           5:hangman.hangman5,
                           6:hangman.hangman6,
                           7:hangman.hangman7,
                           8:hangman.hangman8,
                           9:hangman.hangman9}
    word_to_print = ''
    unsuccessful_tries = len(wrong_guesses_made)

    if check_end.end(wrong_guesses_made, guess) == False:
        return (False, False)

    while True:
        for letter in guess:
            if letter == ' ':
                word_to_print = word_to_print + '_' + ' '
            else:
                word_to_print = word_to_print + letter.upper() + ' '

        message.msg8()
        print(f"""{' '*35 + word_to_print}\n
{'='*90}""")
        hangman_options[unsuccessful_tries]()
        print('='*90)
        user_move = input('\nYOUR GUESS: ').lower()

        if not re.fullmatch(r'[a-z]', user_move):
            message.msg4()
            input()
        elif user_move in wrong_guesses_made or user_move in guess:
            message.msg7()
            input()
        else:
            if user_move not in word:
                message.msg6()
                wrong_guesses_made.append(user_move)
                return (guess, wrong_guesses_made)
            else:
                message.msg9()
                for i in range(len(word)):
                    if word[i] == user_move:
                        guess = guess[:i] + word[i] + guess[i:]
                        return (guess, wrong_guesses_made)
                input()
            input()