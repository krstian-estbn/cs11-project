import os
import time

from engine.game_manager import GameManager

gameManager = GameManager()

def main():
    while True:
        if gameManager.game_loop():
            continue
        else:
            break

if __name__ == "__main__":
    main()
