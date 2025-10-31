class Map:
    def __init__(self):
        pass

    def map_generator(self, level):
        with open(level, "r") as level_loader:
            return [list(line.strip()) for line in level_loader]

    def initial_player_pos(self, level):
        for r, row in enumerate(level):
            for c, cell in enumerate(row):
                    if cell == "L":
                        return (r, c)
