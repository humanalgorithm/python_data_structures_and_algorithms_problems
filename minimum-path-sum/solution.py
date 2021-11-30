class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import sys
        row_len, col_len = len(grid) - 1, len(grid[0]) - 1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                left = sys.maxint
                up = sys.maxint
                if j > 0:
                    left = grid[i][j - 1]
                if i > 0:
                    up = grid[i - 1][j]
                if i > 0 or j > 0:
                    grid[i][j] = min(up, left) + grid[i][j]
        return grid[row_len][col_len]
