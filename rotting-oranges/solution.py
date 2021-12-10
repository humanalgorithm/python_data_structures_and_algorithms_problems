class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        stack, counter = [], 0
        while True:
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if self.checkGrid(i, j, grid):
                        stack.append((i, j))
            if not stack:
                break
            self.updateGrid(stack, grid)
            counter += 1
        done = any(1 in row for row in grid)
        return counter if not done else -1

    def checkGrid(self, i, j, grid):
        if grid[i][j] in [0, 2]:
            return False

        up = grid[i - 1][j] if i > 0 else 0
        down = grid[i + 1][j] if i < len(grid) - 1 else 0
        left = grid[i][j - 1] if j > 0 else 0
        right = grid[i][j + 1] if j < len(grid[i]) - 1 else 0

        if 2 in [up, down, left, right]:
            return True
        return False

    def updateGrid(self, update_stack, grid):
        while update_stack:
            entry = update_stack.pop()
            grid[entry[0]][entry[1]] = 2
