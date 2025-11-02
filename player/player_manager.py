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
            
    def axe(self, map_level, r, c):
        map_level[self.r][self.c] = self.under_l

        # removes tree and removes axe
        self.under_l = '.'
        self.current_item = ''

        self.r, self.c = r, c
        map_level[self.r][self.c] = 'L'
        return
        
    def flamethrower(self, map_level, x, y):
        map_level[self.r][self.c] = self.under_l

        # removes first tree and removes flamethrower
        self.under_l = '.'
        self.current_item = ''

        self.r, self.c = x, y
        map_level[self.r][self.c] = "L"

        # add adjacent trees to player
        burn = set()
        for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (adj[0] + self.r, adj[1] + self.c)
            if 0 <= neighbor[0] < len(map_level) and 0 <= neighbor[1] < len(map_level[0]) and map_level[neighbor[0]][neighbor[1]] == "T":
                            burn.add(neighbor)

        visited = set()
        for neigh in burn:
            adj_trees = [neigh]

            while adj_trees:
                i, j = adj_trees.pop()
                if (i, j) in visited:
                    continue
                
                #remove tree
                visited.add((i, j))
                map_level[i][j] = "."
                
                # add all adjacent trees of the adjacent trees to the list
                for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    neighbor = i + adj[0] , j + adj[1]
                    if 0 <= neighbor[0] < len(map_level) and 0 <= neighbor[1] < len(map_level[0]) and (neighbor[0], neighbor[1]) not in visited:
                        if map_level[neighbor[0]][neighbor[1]] == "T":
                            adj_trees.append((neighbor[0], neighbor[1]))
        
    
    def movement(self, map_level, move, moves, row_len, col_len):
        action = moves[move]
        if callable(action):
            action()
            return 

        dr, dc = action
        new_r, new_c = self.r + dr, self.c + dc


        if not (0 <= new_r < row_len and 0 <= new_c < col_len):
            return 
        
        target_pos = map_level[new_r][new_c]
        
        if target_pos == "T":
            if self.current_item == 'x':
                self.axe(map_level, new_r, new_c)
            elif self.current_item == '*':
                self.flamethrower(map_level, new_r, new_c)
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

        if target_pos in ("+", ".", "-", "x", "*"):
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
