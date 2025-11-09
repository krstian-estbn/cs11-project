import time
import os

from utils.input_handler import InputHandler
from engine.renderer import Renderer
from world.map import Map
from entities.player import Player

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
        time.sleep(0.2)
        return True

    def initialize_game(self, map_file):
        """initialize or reset the game state"""
        try:
            self.map_level = self.maps.map_generator(f"world/{map_file}")
        except FileNotFoundError:
            self.map_level = self.maps.map_generator("world/default_map.txt")
        (r, c), self.mushroom_count = self.maps.initial_player_pos(self.map_level)

        if (r, c) == (-1, -1):
            print("Invalid Map: No 'L' in Map!")
            return False
        
        self.player = Player(r, c)
        self.row_len = len(self.map_level)
        self.col_len = len(self.map_level[0])

        return True

    def game_turn(self, move_input):
        for index, move in enumerate(move_input):
            if move == '!':
                self.initial_movement == move_input[index+1:]
                return '!'
            if move == 'P':
                self.player.pickup_item()
                continue
            if move == 'Q':
                quit()
            self.player.movement(self.map_level, move, self.input_handler.moves, self.row_len, self.col_len)

            if self.player.points == self.mushroom_count:
                if '!' in move_input[index+1:]:
                    self.initial_movement == move_input[index+2:]
                    return '!'
                else:
                    return False
            
            # checks if win condition is satisfied
            if not self.player.status:
                # checks if restart (!) is present
                if move_input[index+1] == '!':
                    self.initial_movement == move_input[index+2:]
                    return '!'
                else:
                    return False
        return 

    def game_loop(self, map, preset_moves, output_file):
        #initialize
        if not self.initialize_game(map):
            return False
         # error handling
        if self.player is None:
            print("Player not Initialized")
            return False
        elif self.map_level is None:
            print("Map Level not Initialized")
            return False
          
        if preset_moves:
            preset_moves = self.input_handler.get_input(preset_moves)
            self.game_turn(preset_moves)
            os.system('cls')
            with open(f"test_folder/{output_file}", "w") as f:
                f.write("CLEAR") if self.player.points == self.mushroom_count else f.write("NO CLEAR")
                for x in self.map_level:
                    f.write("".join(x))
                    f.write("\n")
            return False

        while self.player.status:
            self.renderer.display_map(self.map_level, self.player.points, self.player.under_l, self.player.item.symbol if self.player.item else "")
            try:
                "AA!AA The player must move AA still after the game being reset"
                if self.initial_movement:
                    move_input = self.initial_movement
                else:
                    move_input = self.input_handler.get_input(None)

            except EOFError:
                continue
            
            self.game_turn(move_input)
            if self.initial_movement:
                return self.reset_game()
            self.renderer.display_map(self.map_level, self.player.points, self.player.under_l,  self.player.item.symbol if self.player.item else "")
            if self.player.points == self.mushroom_count:
                print("\n\nYou Won!")
                return False
            else:
                if not self.player.status:
                    print("\n\nGame Over!")
                    return False



            

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

            # checks if it has an output file
            if output_file:
                cleared_status = (self.player.points == self.mushroom_count)
                with open(output_file, "w", encoding="utf-8") as file:
                    file.write("CLEAR\n" if cleared_status else "NO CLEAR\n")
                    for row in self.map_level:
                        file.write("".join(row) + "\n")
                return False

            self.initial_movement = ""
