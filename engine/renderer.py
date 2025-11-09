import os
from termcolor import colored

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

    def display_map(self, map_level, points, under_l, item, mushroom_count, player_status):
        def beautify(level):
            return [[self.emojis.get(cell, cell) for cell in row] for row in level]

        os.system('cls')
        visual_level = beautify(map_level)
        
        for row in visual_level:
            print(*row, sep="")

        print(colored(f"\n{"=" * 32}", "green", attrs=["bold", "dark"]))
        print(f"\n{colored(points, "red", attrs=["bold"]) if points != mushroom_count else colored(points, "yellow", attrs=["bold"])} {colored("out of", "white", attrs=["bold"])} {colored(mushroom_count, "red", attrs=["bold"])} {colored("mushroom(s) collected\n", "white", attrs=["bold"])}")
        
        text_controls = [
            ("[W]", "Move up"),
            ("[A]", "Move left"),
            ("[S]", "Move down"),
            ("[D]", "Move right"),
            ("[!]", "Reset")
        ]
        if points != mushroom_count and player_status:
            for symbol, text in text_controls:
                print(colored(symbol, "blue", attrs=["bold"]), colored(text, "light_cyan", attrs=["bold"]))
            print()
            print((f"{colored("[P]", "blue", attrs=["bold"])} {colored(f"Pick up {self.emojis[under_l]}", "light_cyan", attrs=["bold"])}") if under_l in ("x", "*") else colored("No items here", "red", attrs=["bold", "dark"]))
            print(colored(f"Current holding {self.emojis[item]}", "cyan", attrs=["bold"]) if item is not None else colored("Not holding anything", "light_red", attrs=["bold", "dark"]))
            print(colored(f"\n{"=" * 32}", "green", attrs=["bold", "dark"]))
    
    def end_text(self, player_status):
        if player_status:
            print(colored(r"""__   __         __      __        _ 
\ \ / /__ _  _  \ \    / /__ _ _ | |
 \ V / _ \ || |  \ \/\/ / _ \ ' \|_|
  |_|\___/\_,_|   \_/\_/\___/_||_(_)
                          """, "yellow", attrs=["bold"]))
        else:
            print(colored(r"""__   __          _           _   _ 
\ \ / /__ _  _  | |   ___ __| |_| |
 \ V / _ \ || | | |__/ _ (_-<  _|_|
  |_|\___/\_,_| |____\___/__/\__(_)
                          """, "red", attrs=["bold"]))