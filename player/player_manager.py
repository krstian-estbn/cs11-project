class Player:
    """Handles player behavior"""

    def __init__(self, cur_r, cur_c):
        self.r = cur_r
        self.c = cur_c
        self.points = 0
        self.under_l = "."
        self.under_r = {}
        self.status = True
        self.current_item = ''
        
    def pickup_item(self):
        if self.under_l in ('x', '*'):
            self.current_item = self.under_l
            self.under_l = '.'
        else:
            pass
            
    def axe(self, r, c):
        self.under_l = '.'
        self.current_item = ''
        self.r, self.c = r, c
        return
        
    def flamethrower(self, x, y):
        self.under_l = '.'
        self.current_item = ''
        self.r, self.c = x, y
        return
    
    def movement(self, map_level, move, moves, row_len, col_len):
        action = moves[move]
        if callable(action):
            action()
            return 

        dr, dc = action
        new_r, new_c = self.r + dr, self.c + dc


        if not (0 < new_r < row_len and 0 < new_c < col_len):
            return 
        
        target_pos = map_level[new_r][new_c]
        
        if target_pos == "T":
            if self.current_item == 'x':
                map_level[self.r][self.c] = self.under_l
                self.axe(new_r, new_c)
                map_level[self.r][self.c] = 'L'
            elif self.current_item == '*':
                self.flamethrower(new_r, new_c)
            else:
                return
        # tree function                              

        if target_pos == "R":  
            rock_new_x, rock_new_y = new_r + dr, new_c + dc 
            
            if not (0 <= rock_new_x < row_len and 0 <= rock_new_y < col_len): 
                return 
            
            next_tile = map_level[rock_new_x][rock_new_y] 
            if next_tile in (".", "~", "-"): 
                prev_under_rock = self.under_r.get((new_r, new_c), ".") 
                # checks if there is a previous block before ilagay si rock 
                self.under_r[(rock_new_x, rock_new_y)] = next_tile 
                # updates whatever was under rock 
        
                if next_tile == "~": 
                    map_level[rock_new_x][rock_new_y] = "-" 
                    self.under_r.pop((rock_new_x, rock_new_y), None) 
                    # removes the previous block before rock becauses it became "-" 
                else:
                    map_level[rock_new_x][rock_new_y] = "R"
                
                # returns what was ever under the rock
                map_level[new_r][new_c] = prev_under_rock
                self.under_r.pop((new_r, new_c), None)
                
                # updates what player was under
                map_level[self.r][self.c] = self.under_l 
                
                # si player na ung pumalit sa where rock was stepping into
                self.under_l = prev_under_rock
                map_level[new_r][new_c] = "L"
                
                self.r, self.c = new_r, new_c 
                return
        # rock function

        if target_pos == "~":
            map_level[self.r][self.c] = self.under_l
            map_level[new_r][new_c] = "D"
            self.under_l = "~"
            self.r, self.c = new_r, new_c
            self.status = False
            
            return
        # water function

        if target_pos in ("+", ".", "-", "x"):
            map_level[self.r][self.c] = self.under_l
            if target_pos == "+":
                self.points += 1
                self.under_l = "."
            # mushroom function

            else:
                self.under_l = target_pos
            # concrete and blank function
            
            map_level[new_r][new_c] = "L"
            self.r, self.c = new_r, new_c
            return

        return
        # TANGINA NAG IISANG RETURN NA NAKALIMUTAN KO KAYA NAGCACRASH
