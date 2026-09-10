class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        direcs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        # traverse from treasure outwards and 
        # update values of grid if they are greater than current distance

        def dfs(grid, r, c, dist_treasure):
            for dr, dc in direcs:
                new_r = r + dr
                new_c = c + dc
                if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS:
                    if grid[new_r][new_c] > dist_treasure + 1:
                        grid[new_r][new_c] = dist_treasure + 1
                        dfs(grid, new_r, new_c, dist_treasure + 1)

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(grid, r, c, 0)
        
        return 