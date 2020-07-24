from brain_games.engine import game_launcher
from brain_games.games.prime import run, DESCRIPTION


def main():
    game_launcher(run, DESCRIPTION)


if __name__ == "__main__":
    main()
