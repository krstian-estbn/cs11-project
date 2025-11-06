from engine.game_manager import GameManager
from test_folder import tester
import sys

gameManager = GameManager()

def main():
    while True:
        if len(sys.argv) == 1:
            if gameManager.game_loop("default_map.txt", None, None):
                continue
            else:
                break
        elif len(sys.argv) == 2:
            if gameManager.game_loop(sys.argv[1], None, None):
                continue
            else:
                break
        else:
            gameManager.game_loop(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()
