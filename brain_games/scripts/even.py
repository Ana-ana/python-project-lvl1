from random import randint
from brain_games.scripts.counts import check_even


#  DESCRIPION = 'Answer "yes" if number even otherwise answer "no".'
def DESCRIPION():
    return 'Answer "yes" if number even otherwise answer "no".'


def run():
    cheking_num = randint(0, 1000)
    question = 'Question: ' + str(cheking_num)
    result = check_even(cheking_num)
    return question, result
