import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius! ')
            return True
    else:
        print('You should enter 1~10')


answer = random.randint(1, 10)
while True:
    try:
        guess = int(input('guess a number 1~10: '))
        if (run_guess(guess, answer)):
            break

    except ValueError:
        print('please enter a number')
        continue
