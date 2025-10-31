class InputHandler:
    """Handles input for the player"""

    def __init__(self):
        self.moves = {
            "W": (-1, 0),
            "A": (0, -1),
            "S": (1, 0),
            "D": (0, 1),
            "!": (0, 0),
            "P": (0, 0),
            "Q": (0, 0)
            }

    def get_input(self):
        """Get user input"""

        def get_valid_moves(move_input):
            for ch in move_input:
                if ch not in self.moves:
                    return
                yield ch

        move_input = input("Enter move: ").upper()
        return "".join([*get_valid_moves(move_input)])



