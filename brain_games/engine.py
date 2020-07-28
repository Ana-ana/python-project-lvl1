import prompt


GAME_ROUNDS = 3


def game_launcher(game):
    print('Welcome to the Brain Games!')
    print()
    print(game.DESCRIPION)
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print()
    for _ in range(GAME_ROUNDS):
        question, result = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if str(result) == answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
