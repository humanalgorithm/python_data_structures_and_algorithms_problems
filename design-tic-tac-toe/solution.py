class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """

        self.board = [["-" for x in range(0, n)] for x in range(0, n)]

        self.players = {
            1: "X",
            2: "O"
        }
        self.wins = []

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """

        char = self.players[player]
        self.board[row][col] = char
        check_funcs = [self.check_horizontal, self.check_vertical, self.check_forward_diagonol,
                       self.check_reverse_diagonol]
        for func in check_funcs:
            if func(row, col, char):
                return player
        return 0

    def check_horizontal(self, row, col, char):
        row = self.board[row]
        win = True
        for element in row:
            if element != char:
                win = False
        return win

    def check_vertical(self, row, col, char):
        col_list = []
        for x in range(0, len(self.board[0])):
            col_list += self.board[x][col]
        win = True
        for element in col_list:
            if element != char:
                win = False
        return win

    def check_forward_diagonol(self, row, col, char):
        row_iter = len(self.board) - 1
        col_iter = 0
        win = True
        while row_iter > -1 and col_iter < len(self.board):
            if self.board[row_iter][col_iter] != char:
                win = False
                break
            row_iter -= 1
            col_iter += 1
        return win

    def check_reverse_diagonol(self, row, col, char):
        row_iter = 0
        col_iter = 0
        win = True
        while col_iter < len(self.board) and row_iter < (self.board):
            if self.board[row_iter][col_iter] != char:
                win = False
                break
            row_iter += 1
            col_iter += 1
        return win

    def print_board(self):
        length = len(self.board)

        for i in range(0, length):
            row = ""
            for j in range(0, length):

                # if char == "-"
                row += " | " + self.board[i][j]
                if j == length - 1:
                    row += " |"
            print(row)
        print("")

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)