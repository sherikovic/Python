# Print all possible solutions to N–Queens problem
# The N–queens puzzle is the problem of placing N chess queens on an N × N chessboard so that
# no two queens threaten each other.
# Thus, the solution requires that no two queens share the same row, column, or diagonal.
def solveNQueens(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    backtrack(0)
    if res == []:
        print("It is war!")
    else:
        print(res)


# n = 4
# solveNQueens(n)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
