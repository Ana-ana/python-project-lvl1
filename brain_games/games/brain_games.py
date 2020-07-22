from brain_games.scripts.welcome import welcom_user, welcome


def main():
    welcome()
    name = welcom_user()
    print(name)


if __name__ == '__main__':
    main()
