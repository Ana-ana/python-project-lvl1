from random import randint


DESCRIPION = 'Answer "yes" if number even otherwise answer "no".'


def generate_round():
    question = randint(0, 1000)
    result = ''
    result = 'yes' if question % 2 == 0 else 'no'
    return question, result
