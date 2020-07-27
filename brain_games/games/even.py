from random import randint


DESCRIPION = 'Answer "yes" if number even otherwise answer "no".'


def run():
    cheking_num = randint(0, 1000)
    question = cheking_num
    result = check_even(cheking_num)
    return question, result


def check_even(number):
    """Checks whether number is even"""
    if number % 2 == 0:
        return "yes"
    else:
        return "no"
