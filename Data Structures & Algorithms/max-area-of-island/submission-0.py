class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        max_area = 0
        direcs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def exploreDFS(r, c):
            '''Clear out islands and determine area'''
            stack = [[r, c]]
            area = 1
            while stack:
                rr, cc = stack.pop()
                for dr, dc in direcs:
                    new_r, new_c = rr + dr, cc + dc
                    if new_r >= 0 and new_r < num_rows and new_c >= 0 and new_c < num_cols and grid[new_r][new_c]:
                        stack.append([new_r, new_c])
                        grid[new_r][new_c] = 0
                        area += 1
            
            return area
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c]:
                    grid[r][c] = 0
                    max_area = max(max_area, exploreDFS(r, c))
        return max_area