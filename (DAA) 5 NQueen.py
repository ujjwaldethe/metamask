class NQueens:
    def __init__(self):
        self.size = int(input("Enter size of chessboard: "))
        self.board = [[False] * self.size for _ in range(self.size)]
        self.count = 0

    def printBoard(self):
        for row in self.board:
            for ele in row:
                print("Q" if ele else "X", end=" ")
            print()
        print()

    def isSafe(self, row: int, col: int) -> bool:
        # Check the column
        for i in range(self.size):
            if self.board[i][col]:
                return False
        
        # Check the diagonals
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j]:
                return False
        for i, j in zip(range(row, -1, -1), range(col, self.size)):
            if self.board[i][j]:
                return False
        for i, j in zip(range(row, self.size), range(col, -1, -1)):
            if self.board[i][j]:
                return False
        for i, j in zip(range(row, self.size), range(col, self.size)):
            if self.board[i][j]:
                return False

        return True

    def set_position_first_queen(self):
        print("Enter coordinates of the first queen: ")
        row = int(input(f"Enter row (1-{self.size}): ")) - 1
        col = int(input(f"Enter column (1-{self.size}): ")) - 1
        
        # Ensure the position is valid
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = True
            self.printBoard()
        else:
            print("Invalid coordinates. Please try again.")
            self.set_position_first_queen()  # Retry input

    def solve(self, row: int):
        if row == self.size:
            self.count += 1
            self.printBoard()
            return
        
        # Skip rows that already have a queen
        if any(self.board[row]):
            self.solve(row + 1)
            return

        for col in range(self.size):
            if self.isSafe(row, col):
                self.board[row][col] = True
                self.solve(row + 1)
                self.board[row][col] = False  # Backtrack

    def displayMessage(self):
        if self.count > 0:
            print(f"Total solutions found: {self.count}")
        else:
            print("No solutions exist for the given position of the queen.")

if __name__ == "__main__":
    solver = NQueens()
    solver.set_position_first_queen()
    solver.solve(0)
    solver.displayMessage()
