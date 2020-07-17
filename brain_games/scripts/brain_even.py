import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    print('Answer \"yes\" if number even otherwise answer \"no\".')
    print('')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + "!")
    print('')
    y = 0
    for i in range(3):
        cheking_num = randint(0, 1000)
        print('Question:', cheking_num)
        answer = prompt.string('Your answer :')
        if check_even(cheking_num) == answer:
            print('Correct!')
            print('')
            y += 1
            if y == 3:
                print('Congratulations,', name + '!')
        else:
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print('Let\'s try again,', name + '!')
            break


if __name__ == '__main__':
    main()


def check_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
