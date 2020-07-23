from random import randint


def run():
    i = 0
    y = randint(1, 11)
    begin = randint(1, 11)
    prog = []
    prog.append(str(begin))
    secret = randint(1, 10)
    result = 0
    for i in range(10):
        begin = begin + y
        prog.append(str(begin))
    for item in range(len(prog)):
        if item == secret:
            result = str(prog[item])
            prog[item] = ".."
    progression = ', '.join(prog)
    question = 'Question: ' + progression
    return question, result


def DESCRIPTION():
    return 'What number is missing in the progression?'
