import prompt


ROUNDS_COUNT = 3


def game_launcher(game):
    print('Welcome to the Brain Games!')
    print()
    print(game.DESCRIPION)
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print()
    for _ in range(ROUNDS_COUNT):
        question, result = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if str(result) != answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
