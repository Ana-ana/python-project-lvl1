from random import randint


def run():
    question = randint(1, 11)
    result = ''
    if question > 1:
        if question == 2 or question == 3:
            result = "yes"
        else:
            for i in range(2, question):
                if(question % i) == 0:
                    result = 'no'
                    break
                else:
                    result = 'yes'
    else:
        result = 'no'
    return str(question), result


def DESCRIPTION():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
