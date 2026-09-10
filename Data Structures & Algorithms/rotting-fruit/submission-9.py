class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        queue = collections.deque()
        fresh = 0

        def addCell(r, c):
            nonlocal fresh
            if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                queue.append((r, c))
                fresh -= 1
        
        # find rotten fruit sources and count fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        print(len(queue), fresh)

        # rotten spreading
        time = -1
        while queue:
            print(len(queue))
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRECS:
                    addCell(r + dr, c + dc)
            time += 1

        if fresh != 0:
            return -1
        elif time == -1:
            return 0
        else:
            return time