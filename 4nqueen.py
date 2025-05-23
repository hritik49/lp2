N = int(input("Enter the number of queens: "))
#chessboard
board = [[0]* N for _ in range(N)]

def is_attack(i,j):
    #if the queens are in same columns or row
    for k in range(0,N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    #if the queens in same diagonal
    for k in range(0,N):
        for l in range(0,N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True
    return False

def N_Queen(n):
    if n == 0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (board[i][j]!= 1):
                board[i][j] = 1
                if N_Queen(n-1) == True:
                    return True
                board[i][j] = 0
    return False

N_Queen(N)
print("Board:")
for i in board:
    print(i)
