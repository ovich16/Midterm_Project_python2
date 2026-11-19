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
