from random import randint


DESCRIPION = 'Answer "yes" if number even otherwise answer "no".'


def generate_round():
    question = randint(0, 1000)
    result = check_even(question)
    return question, result


def check_even(number):
    """Checks whether number is even"""
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
