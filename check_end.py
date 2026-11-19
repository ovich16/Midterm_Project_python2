def end(wrong_guesses_made, guess):
    spaces = False
    for letter in guess:
        if letter == ' ':
            spaces = True
    if len(wrong_guesses_made) == 10 or spaces == False:
        return False