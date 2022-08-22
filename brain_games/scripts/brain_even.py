#!/usr/bin/env python3
from brain_games.games import is_parity
from brain_games.games.game_engine import engine


def main():
    print("Brain-even\n\n\nWelcome to the Brain Games!")
    engine(is_parity)


if __name__ == '__main__':
    main()
