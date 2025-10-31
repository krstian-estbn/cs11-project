import time

from utils.input_handler import InputHandler
from engine.renderer import Renderer
from world.map import Map
from player.player_manager import Player


input_handler = InputHandler()
renderer = Renderer()
maps = Map()

class GameManager:
    def __init__(self):
        self.input_handler = InputHandler()
        self.renderer = Renderer()
        self.maps = Map()
        self.player = None
        self.map_level = None
        self.mushrooms = 0
        self.row_len = 0
        self.col_len = 0


    def reset_game(self):
        print("\nResetting game...")
        time.sleep(1)
        return True

    def game_loop(self):
        while self.player.status:
            renderer.display_map(self.map_level, self.player.points, self.player.under_l, self.player.current_item)
            
            try:
                move_input = input_handler.get_input()
            except EOFError:
                continue

            for move in move_input:
                if move == '!':
                    return self.reset_game() 
                if move == 'P':
                    self.player.pickup_item()
                if move == 'Q':
                    quit()
                self.player.movement(self.map_level, move, input_handler.moves, self.row_len, self.col_len)

                if self.player.points == self.mushroom_count:
                    renderer.display_map(self.map_level, self.player.points, self.player.under_l, self.player.current_item)
                    print("\n\nYou Won!")
                    return False
                
                # checks if win condition is satisfied
                if not self.player.status:
                    renderer.display_map(self.map_level, self.player.points, self.player.under_l, self.player.current_item)
                    print("\n\nGame Over!")
                    return False