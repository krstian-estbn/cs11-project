import os

class Renderer:
    def __init__(self):
        self.emojis = {
            "T": "🌲",
            "L": "👨",
            "+": "🍄",
            "R": "🪨 ",
            "~": "🟦",
            "-": "⬜",
            "D": "🏊",
            ".": "　",
            "x": "🪓",
            "*": "🔥",
            "": ""
        }

    def display_map(self, map_level, points, under_l, item, mushroom_count):
        def beautify(level):
            return [[self.emojis.get(cell, cell) for cell in row] for row in level]

        os.system('cls')
        visual_level = beautify(map_level)

        for row in visual_level:
            print(*row, sep="")
        print(f"\nYou Collected: 🍄 {points}/{mushroom_count}")
        print(f"Item below: {self.emojis[under_l]}")
        print(f"Current item: {self.emojis[item]}")