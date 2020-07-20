import prompt


def welcom_user():
    """Welcomes user and asking his or her name"""
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print()
    return name
