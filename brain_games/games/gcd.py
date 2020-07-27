from random import randint
from math import gcd


DESCRIPION = 'Find the greatest common divisor of given numbers.'


def run():
    num1 = randint(0, 1000)
    num2 = randint(0, 1000)
    question = f'{num1} {num2}'
    result = gcd(num1, num2)
    return question, result
