from brain_games.scripts.welcome import welcom_user
from brain_games.scripts.counts import game_calc


def main():
    name = welcom_user()
    print()
    game_calc(name)
