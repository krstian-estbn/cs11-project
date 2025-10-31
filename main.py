import os
import time

from utils.input_handler import InputHandler
from engine.renderer import Renderer
from world.map import Map
from player.player_manager import Player

def game_loop():
    input_handler = InputHandler()
    renderer = Renderer()
    maps = Map()

    map_level = maps.map_generator("test.txt")
    r, c = maps.initial_player_pos(map_level)
    if (r, c) == (-1, -1):
        print("Invalid Map!")
        return

    player = Player(r, c)

    row_len = len(map_level)
    col_len = len(map_level[0])
    
    while player.status:
        renderer.display_map(map_level, player.points, player.under_l)
        
        if not any("+" in row for row in map_level):
            renderer.display_map(map_level, player.points, player.under_l)
            print("\n\nYou Won!")
            return False
        # checks if mushroom still exists

        move_input = input_handler.get_input()
        
        for move in move_input:            
            player.movement(map_level, move, input_handler.moves, row_len, col_len)

            if not player.status:
                renderer.display_map(map_level, player.points, player.under_l)
                print("\n\nGame Over!")
                return False

def main():
    while True:
        if game_loop():
            continue
        else:
            break

if __name__ == "__main__":
    main()