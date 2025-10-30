import os
import time

def map_generator(level):
    with open(level, "r") as level_loader:
        return [list(line.strip()) for line in level_loader]
    # generates a list of the map from the text file

def initial_player_pos(level):
    for r, row in enumerate(level):
        for c, cell in enumerate(row):
                if cell == "L":
                    return (r, c)
    # finds the initial position of the player
def beautify(level):
    emojis = {
        "T": "🌲",
        "L": "👨",
        "+": "🍄",
        "R": "🪨 ",
        "~": "🟦",
        "-": "⬜",
        "D": "🏊",
        ".": "  "
    }
    return [[emojis.get(cell, cell) for cell in row] for row in level]

def display_map(map_level, points):
    os.system('cls')
    visual_level = beautify(map_level)
    for row in visual_level:
        print(*row, sep="")
    print(f"\nYou Collected: {points}🍄")


def user_inputs(moves):
    while True:
        move_input = input("Enter move: ").upper()
        if move_input and all(ch in moves for ch in move_input):
            return move_input
        print("\n\nInvalid moves. Try again.")
        time.sleep(0.8)
        continue

def player_movement(map_level, move, moves, row_len, col_len, cur_r, cur_c, under_l, points):
    dr, dc = moves[move]
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
            if next_tile == "~":
                map_level[rock_new_x][rock_new_y] = "-"
            elif next_tile in (".", "-"):
                map_level[rock_new_x][rock_new_y] = "R"
            
            map_level[cur_r][cur_c] = under_l
            under_l = "."
            map_level[new_r][new_c] = "L"
            cur_r, cur_c = new_r, new_c

            return cur_r, cur_c, under_l, points, True
    # rock function

    if target_pos == "~":
        map_level[cur_r][cur_c] = under_l
        map_level[new_r][new_c] = "D"
        return new_r, new_c, under_l, points, False
    # water function

    if target_pos in ("+", ".", "-"):
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

def main():
    map_level = map_generator("test.txt")
    r, c = initial_player_pos(map_level)
    
    def reset_game():
        print("\nResetting game...")
        time.sleep(1)
        main()
        return

    cur_r, cur_c = r, c
    moves = {
        "W": (-1, 0), "U": (-1, 0),
        "A": (0, -1), "L": (0, -1),
        "S": (1, 0), "J": (1, 0),
        "D": (0, 1), "R": (0, 1),
        "!": reset_game
        }
    row_len = len(map_level)
    col_len = len(map_level[0])
    points = 0
    status = True
    under_l = "."

    while status == True:
        display_map(map_level, points)
        
        if not any("+" in row for row in map_level):
            display_map(map_level, points)
            print("\n\nYou Won!")
            return
        # checks if mushroom still exists

        move_input = user_inputs(moves)
        for move in move_input:
            if move == "!":
                reset_game()
                return
            
            cur_r, cur_c, under_l, points, status = player_movement(
                map_level, move, moves, row_len, col_len, cur_r, cur_c, under_l, points
            )
            display_map(map_level, points)
            time.sleep(0.15)
            if status == False:
                display_map(map_level, points)
                print("\n\nGame Over!")
                return


if __name__ == "__main__":
    main()