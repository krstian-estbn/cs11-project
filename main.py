import os
import keyboard

def map_generator(level):
    map_level = []
    with open(level, "r") as level_loader:
        for _ in level_loader:
            map_level.append(list(_.strip()))
    return map_level
    # generates a list of the map from the text file

def initial_player_pos(level):
    for i in range(len(level)):
        if "P" in level[i]:
            for j in range(len(level[i])):
                if level[i][j] == "P":
                    return (i, j)
    # finds the initial position of the player

def beautify(level):
    emojis = {"T": "🌲",
              "P": "👨",
              "M": "🍄",
              "R": "🪨 ",
              "W": "🟦",
              "C": "⬜",
              " ": "  "
    }
    return [[emojis.get(cell, cell) for cell in row] for row in level]
    
map_level = map_generator("test.txt")
x, y = initial_player_pos(map_level)

cur_x, cur_y = x, y
moves = {"W": (-1, 0),
        "A": (0, -1),
        "S": (1, 0),
        "D": (0, 1)
    }
points = 0
# constants


while True:
    os.system('cls')
    visual_level = beautify(map_level)
    for _ in visual_level:
        print(*_, sep="")
    print(f"\nPoints: {points}")
    # clears and prints map for visualization

    if not any("M" in row for row in map_level):
        os.system('cls')
        break
        # checks if M still exists
    

    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        move = event.name
        # keyboard listener

        if move.upper() in moves:
            dx, dy = moves.get(move.upper())
            new_x, new_y = cur_x + dx, cur_y + dy

            if map_level[new_x][new_y] != "T":

                
                if map_level[new_x][new_y] in ("M", "  ", " ", "C"):
                    if map_level[new_x][new_y] == "M":
                        points += 1
                    map_level[new_x][new_y] = "P"
                    map_level[cur_x][cur_y] = "  "
                    cur_x, cur_y = new_x, new_y
                    

                elif map_level[new_x][new_y] == "R":
                    rock_new_x, rock_new_y = new_x + dx, new_y + dy
                    if map_level[rock_new_x][rock_new_y] in (" ", "  ", "W"):
                        if map_level[rock_new_x][rock_new_y] == "W":
                            map_level[rock_new_x][rock_new_y] = "C"
                        else:
                            map_level[rock_new_x][rock_new_y] = "R"
                        map_level[new_x][new_y] = "P"
                        map_level[cur_x][cur_y] = "  "
                        cur_x, cur_y = new_x, new_y

# end screen?
for _ in visual_level:
        print(*_, sep="")
print(f"\nPoints: {points}")
print("\n\nYou Won")