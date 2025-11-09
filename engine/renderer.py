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
        print(f"\n{points} out of {mushroom_count} mushroom(s) collected\n")

        print("[W] Move up")
        print("[A] Move left")
        print("[S] Move down")
        print("[D] Move right")
        print("[!] Reset\n")
        print(f"[P] Pick up {self.emojis[under_l]}" if under_l in ("x", "*") else "No items here")
        print(f"Current holding {self.emojis[item]}" if item is not None else "Not holding anything\n")