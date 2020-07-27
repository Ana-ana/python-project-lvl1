from random import randint
from math import sqrt


DESCRIPION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run():
    question = randint(1, 11)
    result = is_prime(question)
    return question, result


def is_prime(number):
    if number <= 1:
        return 'no'
    for i in range(2, int(sqrt(number) + 1)):
        if(number % i) == 0:
            return 'no'
    return 'yes'
