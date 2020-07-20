from random import randint
from random import choice
import prompt
from operator import mul, sub, add


#  def sum(num1, num2):
#    return num1 + num2  instead fun operator.add


#  def minus(num1, num2):
#    return num1 - num2 instead fun operator.sub


#  def umnozh(num1, num2):
#    return num1 * num2  instead operator.mul


def game_calc(name):
    y = 0
    operation_list = ['+', '-', '*']
    for i in range(3):
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        operation = choice(operation_list)
        print('Question: ', num1, operation, num2)
        answer = prompt.integer('Your answer: ')
        if (check(num1, num2, operation, answer, name) == "fail"):
            print("Let's try again, ", name, "!")
            break
        y += 1
        if y == 3:
            print('Congratulations, ', name)


def check(num1, num2, operand, answer, name):
    """explanation"""
    if operand == "+":
        result = add(num1, num2)
        if answer == result:
            correct()
        else:
            uncorrect(result, answer, name)
            return "fail"
    elif operand == "-":
        result = sub(num1, num2)
        if answer == result:
            correct()
        else:
            uncorrect(result, answer, name)
            return "fail"
    elif operand == "*":
        result = mul(num1, num2)
        if answer == result:
            correct()
        else:
            uncorrect(result, answer, name)
            return "fail"


def correct():
    print('Correct!')


def uncorrect(result, answer, name):
    print(answer, " is wrong answer ;(. Correct answer was ", result)
    #  print("Let's try again, ", name, "!")
