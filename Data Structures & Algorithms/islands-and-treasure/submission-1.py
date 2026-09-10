class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        # traverse from treasure outwards and 
        # update values of grid if they are greater than current distance

        queue = deque()
        visited = set()

        def addToQueue(r, c):
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and (r, c) not in visited and grid[r][c] > 0:
                queue.append([r, c])
                visited.add((r, c))
            
        # process all source nodes
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addToQueue(r + 1, c)
                addToQueue(r - 1, c)
                addToQueue(r, c + 1)
                addToQueue(r, c - 1)
            dist += 1
        
        return 