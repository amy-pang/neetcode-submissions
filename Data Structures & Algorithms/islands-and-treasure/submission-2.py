class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECS = [[1, 0], [0, -1], [-1, 0], [0, 1]]
        def bfs(treasure_r, treasure_c):
            # update land entries with treasure chest (r, c) if closer
            queue = collections.deque()
            queue.append((treasure_r, treasure_c, 1))
            while queue:
                r, c, dist_from_treasure = queue.popleft()
                for dr, dc in DIRECS:
                    new_r, new_c = r + dr, c + dc
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] > dist_from_treasure:
                        grid[new_r][new_c] = dist_from_treasure
                        queue.append((new_r, new_c, dist_from_treasure + 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r, c)