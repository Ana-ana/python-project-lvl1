import prompt


def game_launcher(run, DESCRIPION):
    print('Welcome to the Brain Games!')
    print()
    print(DESCRIPION())
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    print()
    y = 0
    for i in range(3):
        question, result = run()
        print(question)
        answer = prompt.string('Your answer :')
        if result == answer:
            print('Correct!')
            y += 1
            if y == 3:
                print('Congratulations, ', name, "!")
        else:
            print(answer, " is wrong answer ;(. Correct answer was ", result)
            print("Let's try again, ", name, "!")
            break
