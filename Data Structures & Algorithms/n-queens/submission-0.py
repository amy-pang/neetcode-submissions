class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols, posDiag, negDiag = set(), set(), set()

        def backtrack(subset, y):
            if y == n:
                res.append(subset[:])
                return
            if len(subset) == n:
                return
            
            row = ["." for _ in range(n)]
            for x in range(n): 
                if x not in cols and (y - x) not in negDiag and (x + y) not in posDiag:
                    row[x] = "Q"
                    subset.append("".join(row))
                    cols.add(x)
                    negDiag.add(y - x)
                    posDiag.add(x + y)
                    backtrack(subset, y + 1)
                    
                    row[x] = "."
                    subset.pop()
                    cols.remove(x)
                    negDiag.remove(y - x)
                    posDiag.remove(x + y)

        backtrack([], 0)
        return res