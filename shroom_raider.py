from engine.game_manager import GameManager
from test_folder import tester
import sys
from argparse import ArgumentParser

gameManager = GameManager()

def main():
    parser = ArgumentParser()
    parser.add_argument('-f', '--stage_file', default='world/default_map.txt')
    parser.add_argument('-m', '--moves', default=None)
    parser.add_argument('-o', '--output_file', default=None)
    args = parser.parse_args()
    
    while True:
        if gameManager.game_loop(args.stage_file, args.moves, args.output_file):
            continue
        else:
            break

if __name__ == "__main__":
    main()
