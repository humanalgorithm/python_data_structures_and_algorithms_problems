from collections import defaultdict


class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.horiz_count, self.vert_count = defaultdict(int), defaultdict(int)
        self.diag_down_count, self.diag_up_count = defaultdict(int), defaultdict(int)
        self.n = n
        self.count_moves = 0

    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        funcs = [self.check_horizontal, self.check_vertical,
                 self.check_diag_down, self.check_diag_up]

        for func in funcs:
            if func(player, row=row, col=col):
                return player
        return 0

    def check_horizontal(self, player, row, *args, **kwargs):
        self.horiz_count[(player, row)] += 1
        if self.horiz_count[(player, row)] == self.n:
            return True
        return False

    def check_vertical(self, player, col, *args, **kwargs):
        self.vert_count[(player, col)] += 1
        if self.vert_count[(player, col)] == self.n:
            return True
        return False

    def check_diag_down(self, player, row, col):
        if row == col:
            self.diag_down_count[player] += 1
        if self.diag_down_count[player] == self.n:
            return True
        return False

    def check_diag_up(self, player, row, col):
        if self.n - 1 - row == col:
            self.diag_up_count[player] += 1
        if self.diag_up_count[player] == self.n:
            return True
        return False

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)