class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        valid_directions = {
            1: ['e','w'],
            2: ['n', 's'],
            3: ['s', 'w'],
            4: ['e', 's'],
            5: ['n', 'w'],
            6: ['n', 'e']
        }
        valid_connections = {
            'n': [2,3,4],
            'e': [1,3,5],
            's': [2,5,6],
            'w': [1,4,6]
        }
        
        nrow = len(grid)
        ncol = len(grid[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        def dfs(r,c):
            visited[r][c] = True
            if r == nrow-1 and c == ncol-1:
                return True
            valid = False
            street_num = grid[r][c]
            # n
            if 'n' in valid_directions[street_num] and r > 0 and not visited[r-1][c] and grid[r-1][c] in valid_connections['n']:
                valid = dfs(r-1,c) or valid
            # e
            if 'e' in valid_directions[street_num] and c+1 < ncol and not visited[r][c+1] and grid[r][c+1] in valid_connections['e']:
                valid = dfs(r,c+1) or valid
            # s
            if 's' in valid_directions[street_num] and r+1 < nrow and not visited[r+1][c] and grid[r+1][c] in valid_connections['s']:
                valid = dfs(r+1,c) or valid
            # w
            if 'w' in valid_directions[street_num] and c > 0 and not visited[r][c-1] and grid[r][c-1] in valid_connections['w']:
                valid = dfs(r,c-1) or valid
            return valid
        return dfs(0,0)
        