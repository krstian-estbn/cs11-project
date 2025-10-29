import os
import keyboard

map_level = []
with open("test.txt", "r") as level_loader:
    for _ in level_loader:
        map_level.append(list(_.strip()))
# generates a list of the level from the level text file

for i in range(len(map_level)):
    if "P" in map_level[i]:
        for j in range(len(map_level[i])):
            if map_level[i][j] == "P":
                p_pos = (i, j)
# finds the initial position of the player

x, y = p_pos
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
    for _ in map_level:
        print(*_, sep="")
    print(f"\n Points: {points}")
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
                if map_level[new_x][new_y] == "M":
                    points += 1
                map_level[cur_x][cur_y] = " "
                map_level[new_x][new_y] = "P"
                cur_x, cur_y = new_x, new_y

for _ in map_level:
        print(*_, sep="")
print(f"\nPoints: {points}")
print("\n\nYou Won")