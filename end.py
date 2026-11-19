import message, hangman

def end_game(guess, wrong_guesses_made, word):
    while True:
        if ' ' not in guess:
            message.msg10()
            print(f'(btw the correct word was{word.upper()})')
            print('='*90)
        else:
            message.msg11()
            hangman.hangman10()
            print(f'(btw the correct word was{word.upper()})')
            print('='*90)
            print(f"\n{'='*90}")
        choice = input('ENTER 1 or 2: ')
        if choice == '1':
            return False
        elif choice == '2':
            return True
        else:
            message.msg4()
            input()
