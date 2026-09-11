class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        sq_set = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                sq_num = (i // 3) + ((j // 3) * 3)
                if (board[i][j] in row_set[i] 
                    or board[i][j] in col_set[j]
                    or board[i][j] in sq_set[sq_num]):
                    return False
                row_set[i].add(board[i][j])
                col_set[j].add(board[i][j])
                sq_set[sq_num].add(board[i][j])
        
        return True