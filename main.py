import os
import time

from utils.input_handler import InputHandler
from engine.renderer import Renderer
from world.map import Map

def player_movement(map_level, move, moves, row_len, col_len, cur_r, cur_c, under_l, under_r, points):
    action = moves[move]
    if callable(action):
        action()
        return cur_r, cur_c, under_l, points, True

    dr, dc = action
    new_r, new_c = cur_r + dr, cur_c + dc


    if not (0 <= new_r < row_len and 0 <= new_c < col_len):
        return cur_r, cur_c, under_l, points, True
    
    target_pos = map_level[new_r][new_c]
    
    if target_pos == "T":
        return cur_r, cur_c, under_l, points, True
    # tree function                              

    if target_pos == "R":  
        rock_new_x, rock_new_y = new_r + dr, new_c + dc 
        
        if not (0 <= rock_new_x < row_len and 0 <= rock_new_y < col_len): 
            return cur_r, cur_c, under_l, points, True
        
        next_tile = map_level[rock_new_x][rock_new_y] 
        if next_tile in (".", "~", "-"): 
            prev_under_rock = under_r.get((new_r, new_c), ".") 
            # checks if there is a previous block before ilagay si rock 
            under_r[(rock_new_x, rock_new_y)] = next_tile 
            # updates whatever was under rock 
    
            if next_tile == "~": 
                map_level[rock_new_x][rock_new_y] = "-" 
                under_r.pop((rock_new_x, rock_new_y), None) 
                # removes the previous block before rock becauses it became "-" 
            
            elif next_tile in (".", "-"): 
                map_level[rock_new_x][rock_new_y] = "R"
            
            # returns what was ever under the rock
            map_level[new_r][new_c] = prev_under_rock
            under_r.pop((new_r, new_c), None)
            
            # updates what player was under
            map_level[cur_r][cur_c] = under_l 
            
            # si player na ung pumalit sa where rock was stepping into
            under_l = prev_under_rock
            map_level[new_r][new_c] = "L"
            
            cur_r, cur_c = new_r, new_c 
            return cur_r, cur_c, under_l, points, True
    # rock function

    if target_pos == "~":
        map_level[cur_r][cur_c] = under_l
        map_level[new_r][new_c] = "D"
        under_l = "~"
        cur_r, cur_c = new_r, new_c
        
        return cur_r, cur_c, under_l, points, False
    # water function

    if target_pos in ("+", ".", "-", "x"):
        map_level[cur_r][cur_c] = under_l
        if target_pos == "+":
            points += 1
            under_l = "."
        # mushroom function

        else:
            under_l = target_pos
        # concrete and blank function
        
        map_level[new_r][new_c] = "L"
        cur_r, cur_c = new_r, new_c
        return cur_r, cur_c, under_l, points, True

    return cur_r, cur_c, under_l, points, True
    # TANGINA NAG IISANG RETURN NA NAKALIMUTAN KO KAYA NAGCACRASH

def game_loop():
    input_handler = InputHandler()
    renderer = Renderer()
    maps = Map()

    map_level = maps.map_generator("test.txt")
    r, c = maps.initial_player_pos(map_level)
    if (r, c) == (-1, -1):
        print("Invalid Map!")
        return

    cur_r, cur_c = r, c

    row_len = len(map_level)
    col_len = len(map_level[0])
    
    points = 0
    status = True
    under_l = "."
    under_r = {}

    while status == True:
        renderer.display_map(map_level, points, under_l)
        
        if not any("+" in row for row in map_level):
            renderer.display_map(map_level, points, under_l)
            print("\n\nYou Won!")
            return False
        # checks if mushroom still exists

        move_input = input_handler.get_input()
        
        for move in move_input:            
            cur_r, cur_c, under_l, points, status = player_movement(
                map_level, move, input_handler.moves, row_len, col_len, cur_r, cur_c, under_l, under_r, points
            )

            if status == False:
                renderer.display_map(map_level, points, under_l)
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