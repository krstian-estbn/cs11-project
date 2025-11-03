class Item:
    def __init__(self, symbol):
        self.symbol = symbol

    def use(self, map_level, under_l, player_r, player_c, r, c):
        if self.symbol == "x":
            return self.chop_tree(map_level, under_l, player_r, player_c, r, c)

        elif self.symbol == "*":
            return self.burn_trees(map_level, under_l, player_r, player_c, r, c)

    def chop_tree(self, map_level, under_l, player_r, player_c, target_r, target_c):
        map_level[player_r][player_c] = under_l

        # removes tree and removes axe
        under_l = '.'

        player_r, player_c = target_r, target_c
        map_level[player_r][player_c] = 'L'

        return under_l, player_r, player_c

    def burn_trees(self, map_level, under_l, player_r, player_c, target_r, target_c):
        map_level[player_r][player_c] = under_l

        # removes first tree and removes flamethrower
        under_l = '.'

        player_r, player_c = target_r, target_c
        map_level[player_r][player_c] = "L"

        # add adjacent trees to player
        burn = set()
        for adj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (adj[0] + player_r, adj[1] + player_c)
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
        
        return under_l, player_r, player_c