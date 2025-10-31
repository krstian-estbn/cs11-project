class Map:
    def __init__(self):
        pass

    def map_generator(self, level):
        with open(level, "r", encoding="utf-8") as level_loader:
            return [list(line.strip()) for line in level_loader]

    def initial_player_pos(self, level):
        s = (-1, -1)
        m = 0
        for r, row in enumerate(level):
            for c, cell in enumerate(row):
                    if cell == '+':
                        m += 1 
                        continue
                    if cell == "L":
                        s = (r, c)
        return (s, m)
