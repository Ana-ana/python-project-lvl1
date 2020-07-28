import operator
from random import randint, choice


DESCRIPION = 'What is the result of the expression?'


def generate_round():
    """Function to play calculation game"""
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = choice(list(operators.keys()))
    question = f'{num1} {operation} {num2}'
    result = operators[operation](num1, num2)
    return question, result
