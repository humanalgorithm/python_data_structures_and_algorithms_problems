class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        """
        original new conv
         0        0    0
         1        0    1
         0        1    2
         1        1    3
        """
        conv_to_orig = {0: 0, 1: 1, 2: 0, 3: 1}
        conv_to_new = {0: 0, 1: 0, 2: 1, 3: 1}

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                self.calculateCell(i, j, board, conv_to_orig)

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                board[i][j] = conv_to_new.get(board[i][j])

    def calculateCell(self, i, j, board, conv_to_orig):
        left = board[i][j - 1] if j > 0 else 0
        right = board[i][j + 1] if j < len(board[i]) - 1 else 0
        up = board[i - 1][j] if i > 0 else 0
        down = board[i + 1][j] if i < len(board) - 1 else 0

        left_up = board[i - 1][j - 1] if (j > 0 and i > 0) else 0
        right_up = board[i - 1][j + 1] if (j < len(board[i]) - 1 and i > 0) else 0
        left_down = board[i + 1][j - 1] if (j > 0 and i < len(board) - 1) else 0
        right_down = board[i + 1][j + 1] if (j < len(board[i]) - 1 and i < len(board) - 1) else 0

        cross_sum = sum([conv_to_orig.get(item) for item in [left, right, up, down]])
        diag_sum = sum([conv_to_orig.get(item) for item in [left_up, right_up,
                                                            left_down, right_down]])

        self.writeBoard(board, i, j, cross_sum + diag_sum)

    def writeBoard(self, board, i, j, total_sum):
        original = board[i][j]
        if original in (1, 3):
            new = self.calculateLive(total_sum)
            board[i][j] = 1 if new == 0 else 3
        else:
            new = self.calculateDead(total_sum)
            board[i][j] = 0 if new == 0 else 2

    def calculateLive(self, total_sum):
        if total_sum < 2:
            return 0
        elif total_sum in [2, 3]:
            return 1
        elif total_sum > 3:
            return 0

    def calculateDead(self, total_sum):
        if total_sum == 3:
            return 1
        return 0
