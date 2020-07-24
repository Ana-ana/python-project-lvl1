from random import randint


def run():
    PROGRESSION_LENGTH_LIMIT = 10
    step = randint(1, 11)
    begin = randint(1, 11)
    prog = []
    secret = randint(0, PROGRESSION_LENGTH_LIMIT)
    result = 0
    for i in range(PROGRESSION_LENGTH_LIMIT):
        begin = begin + step
        prog.append(str(begin))
        if i == secret:
            result = str(prog[i])
            prog[i] = ".."
    question = ', '.join(prog)
    print(result)
    return question, result


def DESCRIPTION():
    return 'What number is missing in the progression?'

