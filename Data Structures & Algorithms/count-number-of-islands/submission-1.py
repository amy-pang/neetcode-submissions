class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def exploreBFS(r, c):
            queue = deque()
            queue.append([r, c])

            while queue:
                rr, cc = queue.popleft()
                if (rr, cc) not in visited and grid[rr][cc] == "1":
                    visited.add((rr, cc))
                    direc = [[1,0], [-1,0], [0, 1], [0, -1]]
                    for dr, dc in direc:
                        rrr = int(rr) + dr
                        ccc = int(cc) + dc
                        if (rrr, ccc) not in visited and rrr >= 0 and rrr < rows and ccc >= 0 and ccc < cols:
                            queue.append([rrr, ccc])

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    exploreBFS(r, c)
                    num_islands += 1
        
        return num_islands
        
