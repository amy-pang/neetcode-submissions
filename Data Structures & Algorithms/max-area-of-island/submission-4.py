class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        DIREC = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c):
            stack = [[r, c]]
            grid[r][c] = 0
            area = 1
            while stack:
                r, c = stack.pop()
                print("dfs: r, c", r, c)
                for dr, dc in DIREC:
                    new_r = r + dr
                    new_c = c + dc
                    print("new_r, new_c", new_r, new_c)
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == 1:
                        stack.append([new_r, new_c])
                        area += 1
                        grid[new_r][new_c] = 0
            print(area)
            return area
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    print("starting dfs", r, c)
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
