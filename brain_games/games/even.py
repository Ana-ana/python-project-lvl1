from random import randint


DESCRIPION = 'Answer "yes" if number even otherwise answer "no".'


def generate_round():
    question = randint(0, 1000)
    result = ''
    if is_even(question):
        result = 'yes'
    else:
        result = 'no'
    return question, result


def is_even(number):
    """Checks whether number is even"""
    if number % 2 == 0:
        return True
    else:
        return False
