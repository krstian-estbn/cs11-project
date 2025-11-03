import time

from utils.input_handler import InputHandler
from engine.renderer import Renderer
from world.map import Map
from player.player_manager import Player

class GameManager:
    def __init__(self):
        self.input_handler = InputHandler()
        self.renderer = Renderer()
        self.maps = Map()
        self.player = None
        self.map_level = None
        self.mushroom_count = 0
        self.row_len = 0
        self.col_len = 0
        self.initial_movement = ""


    def reset_game(self):
        print("\nResetting game...")
        time.sleep(0.5)
        return True

    def initialize_game(self, map_file="test.txt"):
        """initialize or reset the game state"""
        self.map_level = self.maps.map_generator(map_file)
        (r, c), self.mushroom_count = self.maps.initial_player_pos(self.map_level)

        if (r, c) == (-1, -1):
            print("Invalid Map: No 'L' in Map!")
            return False
        
        self.player = Player(r, c)
        self.row_len = len(self.map_level)
        self.col_len = len(self.map_level[0])

        return True

    def game_loop(self):

        #initialize
        if not self.initialize_game():
            return False

        while self.player.status:
            self.renderer.display_map(self.map_level, self.player.points, self.player.under_l, self.player.item.symbol if self.player.item else "")
            
            try:
                "AA!AA The player must move AA still after the game being reset"
                if self.initial_movement:
                    move_input = self.initial_movement
                else:
                    move_input = self.input_handler.get_input()

            except EOFError:
                continue

            for move in move_input:
                if move == '!':
                    self.initial_movement = move_input.split('!', 1)[1]
                    return self.reset_game() 
                if move == 'P':
                    self.player.pickup_item()
                if move == 'Q':
                    quit()
                self.player.movement(self.map_level, move, self.input_handler.moves, self.row_len, self.col_len)

                if self.player.points == self.mushroom_count:
                    if '!' not in move_input:
                        self.renderer.display_map(self.map_level, self.player.points, self.player.under_l,  self.player.item.symbol if self.player.item else "")
                        print("\n\nYou Won!")
                        return False
                    else:
                        self.initial_movement = move_input.split('!', 1)[1]
                        return self.reset_game()
                
                # checks if win condition is satisfied
                if not self.player.status:
                    # checks if restart (!) is present
                    if '!' not in move_input:
                        self.renderer.display_map(self.map_level, self.player.points, self.player.under_l, self.player.item.symbol if self.player.item else "")
                        print("\n\nGame Over!")
                        return False
                    else:
                        self.initial_movement = move_input.split('!', 1)[1]
                        return self.reset_game()
            self.initial_movement = ""