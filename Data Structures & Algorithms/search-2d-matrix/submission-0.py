class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows - 1
        row = 0;
        while l <= r:
            m = (r + l) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][cols -1] < target:
                l = m + 1
            else: 
                row = m
                break

        l, r = 0, cols - 1
        while l <= r:
            m = (r + l) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m -1
            else:
                return True

        return False