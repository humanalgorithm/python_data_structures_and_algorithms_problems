import copy


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        processed_board = self.processBoard(board)
        board[:] = []
        [board.append(element) for element in processed_board]

    def processBoard(self, board):
        board_copy = copy.deepcopy(board)
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                num_neighbors = self.get_number_of_neighbors(board, i, j)
                self.applyRules(i, j, num_neighbors, board_copy, board)
        return board_copy

    def applyRules(self, i, j, num_neighbors, board_copy, board):
        rules = [self.less_than_two, self.two_or_three, self.more_than_three, self.three_live]
        for rule in rules:
            rule_apply = rule(num_neighbors, board[i][j])
            if rule_apply[0]:
                board_copy[i][j] = rule_apply[1]
                break

    def less_than_two(self, num_neighbors, current_element):
        if num_neighbors < 2 and current_element == 1:
            return (True, 0)
        return (False, current_element)

    def two_or_three(self, num_neighbors, current_element):
        if (num_neighbors == 2 or num_neighbors == 3) and current_element == 1:
            return (True, 1)
        return (False, current_element)

    def more_than_three(self, num_neighbors, current_element):
        if num_neighbors > 3 and current_element == 1:
            return (True, 0)
        return (False, current_element)

    def three_live(self, num_neighbors, current_element):
        if num_neighbors == 3 and current_element == 0:
            return (True, 1)
        return (False, current_element)

    def get_number_of_neighbors(self, board, i, j):
        north = (i - 1, j)
        south = (i + 1, j)
        west = (i, j - 1)
        east = (i, j + 1)
        northwest = (i - 1, j - 1)
        northeast = (i - 1, j + 1)
        southwest = (i + 1, j - 1)
        southeast = (i + 1, j + 1)

        sum_nums = 0
        for pos in [north, south, west, east, northwest, northeast, southwest, southeast]:
            if pos[0] < 0 or pos[1] < 0:
                continue
            try:
                num = board[pos[0]][pos[1]]
            except Exception:
                num = 0
            sum_nums = sum_nums + num
        return sum_nums
