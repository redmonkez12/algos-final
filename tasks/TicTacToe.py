class TicTacToe:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def check_state(self, moves: list[list[int]]) -> str:
        for i, move in enumerate(moves):
            row, col = move

            player = "O"

            if i % 2 == 0:
                player = "X"

            self.grid[row][col] = player

            if self.check_winner(player):
                return player

        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

    def check_winner(self, player: str) -> bool:
        for row in self.grid:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.grid[row][col] == player for row in range(3)):
                return True

        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == player:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == player:
            return True

        return False

    def print_board(self):
        for row in self.grid:
            print('|', end='')
            for cell in row:
                print(cell, end='|')
            print()


tictactoe = TicTacToe()
moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
result = tictactoe.check_state(moves)
tictactoe.print_board()
# print(result)

# for col in range(3):
#     for row in range(3):
#         print(col, row)