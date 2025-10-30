import os
import time

def map_generator(level):
    map_level = []
    with open(level, "r") as level_loader:
        for _ in level_loader:
            map_level.append(list(_.strip()))
    return map_level
    # generates a list of the map from the text file

def initial_player_pos(level):
    for row in range(len(level)):
        if "L" in level[row]:
            for col in range(len(level[row])):
                if level[row][col] == "L":
                    return (row, col)
    # finds the initial position of the player

def beautify(level):
    emojis = {"T": "🌲",
              "L": "👨",
              "+": "🍄",
              "R": "🪨 ",
              "~": "🟦",
              "-": "⬜",
              "D": "🏊",
              ".": "  "
    }
    return [[emojis.get(cell, cell) for cell in row] for row in level]
    
map_level = map_generator("test.txt")
r, c = initial_player_pos(map_level)

cur_r, cur_c = r, c
moves = {"W": (-1, 0),
        "A": (0, -1),
        "S": (1, 0),
        "D": (0, 1)
    }
row_len = len(map_level)
col_len = len(map_level[0])
points = 0
status = True
under_l = "."
# constants


while status == True:
    os.system('cls')

    visual_level = beautify(map_level)
    for _ in visual_level:
        print(*_, sep="")
    print(f"\nPoints: {points}")
    # clears and prints map for visualization

    if not any("+" in row for row in map_level):
        os.system('cls')
        break
        # checks if mushroom still exists

    move_input = input("Enter move: ")

    for move in move_input.upper():
        if move in moves:
            dr, dc = moves.get(move.upper())
            new_r, new_c = cur_r + dr, cur_c + dc


            if not (0 <= new_r < row_len and 0 <= new_c < col_len):
                continue
            
            target_pos = map_level[new_r][new_c]
            if target_pos == "T":
                continue
                              

            if target_pos == "R":
                rock_new_x, rock_new_y = new_r + dr, new_c + dc

                if not (0 <= rock_new_x < row_len and 0 <= rock_new_y < col_len):
                    continue

                next_tile = map_level[rock_new_x][rock_new_y]
                
                if next_tile in (".", "~", "-"):
                    if next_tile == "~":
                        map_level[rock_new_x][rock_new_y] = "-"
                    elif next_tile in (".", "-"):
                        map_level[rock_new_x][rock_new_y] = "R"
                    
                    map_level[cur_r][cur_c] = under_l
                    under_l = "."
                    map_level[new_r][new_c] = "L"
                    cur_r, cur_c = new_r, new_c
            
            if target_pos == "~":
                map_level[cur_r][cur_c] = "."
                target_pos = "D"
                status = False


            if target_pos in ("+", ".", "-"):
                map_level[cur_r][cur_c] = under_l
                if target_pos == "+":
                    points += 1
                    under_l = "."
                else:
                    under_l = target_pos
                
                
                map_level[new_r][new_c] = "L"
                cur_r, cur_c = new_r, new_c
            
            os.system('cls')
            visual_level = beautify(map_level)
            for _ in visual_level:
                print(*_, sep="")
            print(f"\nPoints: {points}")
            print("Enter move: ")
            time.sleep(0.2) 

# end screen?
if status == True:
    for _ in visual_level:
            print(*_, sep="")
    print(f"\nPoints: {points}")
    print("\n\nYou Won")

else:
    for _ in visual_level:
            print(*_, sep="")
    print(f"\nPoints: {points}")
    print("\n\nGame Over!")