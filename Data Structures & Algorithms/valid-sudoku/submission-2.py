class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols, rows, sqs = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in (cols[c] | rows[r] | sqs[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqs[(r // 3, c // 3)].add(board[r][c])

        return True