from argparse import ArgumentParser

from engine.game_manager import GameManager

gameManager = GameManager()
parser = ArgumentParser()
parser.add_argument("-f", "--stage_file", default="world/default_map.txt")
parser.add_argument("-m", "--moves", default=None)
parser.add_argument("-o", "--output_file", default=None)
args = parser.parse_args()


def main():
    while True:
        if gameManager.game_loop(args.stage_file, args.moves, args.output_file):
            continue
        else:
            break


if __name__ == "__main__":
    main()
