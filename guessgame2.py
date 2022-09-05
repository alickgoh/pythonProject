import random


def guess_algorithm():
    ini_guess = 50
    guess_count = 0
    guess_check = False
    while guess_check is not True:
        guess = input(f'My guess is {ini_guess}, Was it right?\n'
                      f'H/L/Y , H for too high, L for too low, Y for correct answer\n'
                      f'>>>')
        guess_count += 1
        if guess.lower() == 'l':
            ini_guess += 1
        elif guess.lower() == 'h':
            ini_guess -= 1
        if guess.lower() == 'y':
            guess_check = True
            print(f'Your guess is correct!'
                  f'Your guess count is {guess_count}')
        else:
            print('i dont understand that!')


guess_algorithm()
