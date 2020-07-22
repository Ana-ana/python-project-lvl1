from random import randint
from math import gcd


def run():
    num1 = randint(0, 1000)
    num2 = randint(0, 1000)
    question = str(num1) + ' ' + str(num2)
    result = gcd(num1, num2)
    return question, result


def DESCRIPTION():
    return 'Find the greatest common divisor of given numbers.'
