valid_guesses = set()

with open('valid_guesses.txt', 'r') as f:
    for line in f:
        valid_guesses.add(line.strip())


def is_valid_guess(guess):
    return guess in valid_guesses
