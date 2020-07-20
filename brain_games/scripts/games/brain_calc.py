from brain_games.scripts.welcome import welcom_user
from brain_games.scripts.counts import game_calc


def main():
    print('Welcome to the Brain Games!')
    print()
    print('What is the result of the expression?')
    name = welcom_user()
    game_calc(name)


if __name__ == '__main__':
    main()
