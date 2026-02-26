'''
Place N queens on an N x N chessboard such that no queens attack eachother.
'''

def solveNQueens(n):
    board = [["."] * n for _ in range(n)]
    result = []
    
    def is_safe(row, col):
        # check column
        for i in range(row):
            if board[i][col] == "Q":
                return False
            
        i, j = row - 1, col - 1
        while i >=0 and j >=0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j-= 1
            
        return True
    def backtrack(row):
        if row == n:
            #save solution 
            result.append(["".join(r) for r in board])
            return 
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = "Q" # place the queen
                backtrack(row + 1)
                board[row][col] = "."  # remove queen (backtrack)
    
    
    backtrack(0)
    return result

solutions = solveNQueens(4)

for sol in solutions:
    for row in sol:
        print(row)
    print()                