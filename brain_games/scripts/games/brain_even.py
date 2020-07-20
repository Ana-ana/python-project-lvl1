import prompt
from random import randint
from brain_games.scripts.welcome import welcom_user
from brain_games.scripts.counts import check_even


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    print('')
    name = welcom_user()
    y = 0
    for i in range(3):
        cheking_num = randint(0, 1000)
        print('Question:', cheking_num)
        answer = prompt.string('Your answer :')
        result = check_even(cheking_num)
        if result == answer:
            print('Correct!')
            print('')
            y += 1
            if y == 3:
                print('Congratulations,', name + '!')
        else:
            print(answer, ' is wrong answer ;(. Correct answer was ', result)
            print('Let\'s try again,', name + '!')
            break


if __name__ == '__main__':
    main()
