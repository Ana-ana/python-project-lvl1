#  from operator import mul, sub, add
import operator
from random import randint
from random import choice


#  DESCRIPION = "What is the result of the expression?"
def DESCRIPION():
    return 'What is the result of the expression?'


def run():
    """Function to play calculation game"""
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    oper = list(operators.keys())
    operation = choice(oper)
    #  print('Question: ', num1, operation, num2)
    question = 'Question:' + str(num1) + ' ' + str(operation) + ' ' + str(num2)
    result = str(operators[operation](num1, num2))
    return question, result
