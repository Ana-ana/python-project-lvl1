from random import randint
from math import sqrt


DESCRIPION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_round():
    question = randint(1, 11)
    result = 'yes' if is_prime(question) else 'no'
    return question, result


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
