import random

def get_word(guesses_made):
    with open('words.txt') as f:
        words = f.read().split()

    suitable = []
    for word in words:
        accepted = True
        for letter in guesses_made:
            if letter in word:
                accepted = False
        if accepted == True:
            suitable.append(word)
    
    return random.choice(suitable)