from random import randint


DESCRIPION = 'What number is missing in the progression?'
PROGRESSION_LENGTH_LIMIT = 10


def run():
    step = randint(1, 11)
    begin = randint(1, 11)
    prog = []
    secret = randint(0, PROGRESSION_LENGTH_LIMIT)
    result = 0
    for i in range(PROGRESSION_LENGTH_LIMIT - 1):
        begin = begin + step
        prog.append(str(begin))
        if i == secret:
            result = prog[i]
            prog[i] = '..'
    question = ', '.join(prog)
    return question, result
