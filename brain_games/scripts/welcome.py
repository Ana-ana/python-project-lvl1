import prompt


def welcom_user():
    """Welcomes user and asking his or her name"""
    print('Welcome to the Brain Games!')
    print()
    print('What is the result of the expression?')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    return name
