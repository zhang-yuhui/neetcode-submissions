class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s1 = set()
        s2 = set()
        for i in range(9):
            s1.clear()
            s2.clear()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] not in s1:
                        s1.add(board[i][j])
                    else:
                        return False

                if board[j][i] != '.':
                    if board[j][i] not in s2:
                        s2.add(board[j][i])
                    else:
                        return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s1.clear()
                for ii in range(i, i+3):
                    for jj in range(j, j+3):
                        x = board[ii][jj]
                        if x != '.':
                            if x not in s1:
                                s1.add(x)
                            else:
                                return False
        
        return True