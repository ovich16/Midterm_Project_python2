import hangman, re, message

def fake_move(wrong_guesses_made):
    unsuccessful_tries = len(wrong_guesses_made)
    hangman_options = {0:hangman.hangman0,
                       1:hangman.hangman1,
                       2:hangman.hangman2}

    while True:
        message.msg5()
        hangman_options[unsuccessful_tries]()
        print('\n' + '='*90)
        user_move = input('\nYOUR GUESS: ').lower()
        if re.fullmatch(r'[a-z]', user_move) and user_move not in wrong_guesses_made:
            wrong_guesses_made.append(user_move)
            message.msg6()
            input()
            break
        elif user_move in wrong_guesses_made:
            message.msg7()
            input()
        else:
            message.msg4()
            input()
    return wrong_guesses_made