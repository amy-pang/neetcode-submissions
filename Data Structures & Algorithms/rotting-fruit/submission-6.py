class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # find all sources (rotten bananas) and move outwards
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        queue = deque()
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                elif grid[r][c] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        def addToQueue(r, c):
            nonlocal num_fresh
            if min(r, c) >= 0 and r < ROWS and c < COLS and grid[r][c] == 1:
                queue.append([r, c])
                grid[r][c] = 2
                num_fresh -= 1
            
        while num_fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                addToQueue(r + 1, c)
                addToQueue(r - 1, c)
                addToQueue(r, c + 1)
                addToQueue(r, c - 1)
            time += 1
            print(queue)

        return time if num_fresh == 0 else -1
