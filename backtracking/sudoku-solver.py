def solveSudoku(board):
    def is_valid(r, c, num):
        # check row
        for i in range(9):
            if board[r][i] == num:
                return False
            
        # check column
        for i in range(9):
            if board[i][c] == num:
                return False
            
        # check 3x3 box
        start_r = (r // 3) * 3
        start_c = (c // 3) * 3
        
        for i in range(3):
            for j in range(3):
                if board[start_r + i][start_c + j] == num:
                    return False
        return True
    
    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] ="."
                    return False
        return True
    
    backtrack()
    
board = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]

solveSudoku(board)

for row in board:
    print(row)