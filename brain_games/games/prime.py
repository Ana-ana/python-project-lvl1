from random import randint


def run():
    question = randint(1, 11)
    result = is_prime(question)
    return str(question), result


def DESCRIPTION():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number > 1:
        if number == 2 or number == 3:
            return 'yes'
        else:
            for i in range(2, number):
                if(number % i) == 0:
                    return 'no'
                    break
                else:
                    return 'yes'
    else:
        return 'no'
