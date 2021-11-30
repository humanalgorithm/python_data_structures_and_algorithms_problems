class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        board_copy = [[item for item in board[x]] for x in range(0, len(board))]

        for i in range(0, len(board_copy)):
            for j in range(0, len(board_copy[i])):
                result = self.calculateCell(i, j, board_copy)
                board[i][j] = result

    def calculateCell(self, i, j, board):
        left = board[i][j - 1] if j > 0 else 0
        right = board[i][j + 1] if j < len(board[i]) - 1 else 0
        up = board[i - 1][j] if i > 0 else 0
        down = board[i + 1][j] if i < len(board) - 1 else 0

        left_up = board[i - 1][j - 1] if (j > 0 and i > 0) else 0
        right_up = board[i - 1][j + 1] if (j < len(board[i]) - 1 and i > 0) else 0
        left_down = board[i + 1][j - 1] if (j > 0 and i < len(board) - 1) else 0
        right_down = board[i + 1][j + 1] if (j < len(board[i]) - 1 and i < len(board) - 1) else 0

        cross_sum = sum([left, right, up, down])
        diag_sum = sum([left_up, right_up, left_down, right_down])

        if board[i][j] == 1:
            return self.calculateLive(cross_sum + diag_sum)
        else:
            return self.calculateDead(cross_sum + diag_sum)

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
