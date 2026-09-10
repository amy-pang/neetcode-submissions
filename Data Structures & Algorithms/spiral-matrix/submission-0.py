class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        x, y, dx, dy = 0, 0, 1, 0
        height, width = len(matrix), len(matrix[0])
        for _ in range(height * width):
            res.append(matrix[y][x])
            matrix[y][x] = "."
            if not 0 <= x + dx < width or not 0 <= y + dy < height or matrix[y +dy][x+dx] == ".":
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        return res