def welcome_message():
    while True:
        print(f"""\033[2J\033[H", end=\n
{' '*20}😈😈😈 WELCOME TO THE EVIL HANGMAN GAME!!! 😈😈😈
{'='*90}
The rules are simple — guess the word I'm thinking of. (but I will be cheating)
You can choose how much I will cheat entering the level of difficulty. 
{'='*90}""")
        try:
            diff_choice = int(input('ENTER A NUMBER BETWEEN 1 and 3: '))
            if 4 > diff_choice > 0:
                print(f"""{'='*90}
{' '*30}Okay! Press ENTER to start ⎛⎝( ` ᢍ ´ )⎠⎞""")
                input()
                break
            else:
                print(f"""{'='*90}
{' '*28}Value out of range! Press ENTER to try again.""")
                input()
        except:
            print(f"""{'='*90}
{' '*10}This value cannot be entered! Press ENTER to try again.""")
            input()
    return diff_choice