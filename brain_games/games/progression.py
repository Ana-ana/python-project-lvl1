from random import randint


DESCRIPION = 'What number is missing in the progression?'
PROGRESSION_LENGTH_LIMIT = 10


def generate_round():
    step = randint(1, 11)
    begin = randint(1, 11)
    progression = []
    secret = randint(0, PROGRESSION_LENGTH_LIMIT - 1)
    for i in range(PROGRESSION_LENGTH_LIMIT):
        progression.append(begin + step * i)
    result = begin + step * secret
    progression[secret] = '..'
    print('result is ', result)
    question = ', '.join(str(num) for num in progression)
    return question, result
