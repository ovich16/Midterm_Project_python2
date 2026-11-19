def msg1():
    print(f"""\033[2J\033[H", end=\n
{' '*20}😈😈😈 WELCOME TO THE EVIL HANGMAN GAME!!! 😈😈😈
{'='*90}\n
The rules are simple — guess the word I'm thinking of. (but I will be cheating)
You can choose how much I will cheat by entering the level of difficulty.\n
{'='*90}""")

def msg2():
    print(f"""{'='*90}
{' '*30}Okay! Press ENTER to start ⎛⎝( ` ᢍ ´ )⎠⎞""")

def msg3():
    print(f"""{'='*90}
{' '*23}Value out of range! Press ENTER to try again.""")

def msg4():
    print(f"""{'='*90}
{' '*17}This value cannot be entered! Press ENTER to try again.""")

def msg5():
    print(f"""\033[2J\033[H", end=\n
{' '*19}😈😈😈 TRY TO GUESS THE WORD I AM THINKING OF! 😈😈😈
{'='*90}\n
Enter a letter that you think is in the word below.\n
{'='*90}\n
{' '*35 + '_ '*9}\n
{'='*90}\n""")

def msg6():
    print(f"""\n{'='*90}
{' '*27}😈😈😈 YOUR GUESS IS WRONG! 😈😈😈
press ENTER to try again.
{'='*90}""")

def msg7():
    print(f"""\n{'='*90}
{' '*23}😈😈😈 YOU'VE ALREADY TRIED THIS LETTER! 😈😈😈
press ENTER to try again.
{'='*90}""")

def msg8():
    print(f"""\033[2J\033[H", end=\n
{' '*19}😈😈😈 TRY TO GUESS THE WORD I AM THINKING OF! 😈😈😈
{'='*90}\n
Enter a letter that you think is in the word below.\n
{'='*90}\n""")