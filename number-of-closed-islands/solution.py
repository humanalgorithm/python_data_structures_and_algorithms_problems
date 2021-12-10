class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = []
        result = 0
        m, n = len(grid), len(grid[0])

        for i in range(0, m):
            for j in range(0, n):
                isClosed = False
                if grid[i][j] == 0:
                    queue.append((i, j))
                    grid[i][j] = 1
                    isClosed = True

                while queue:
                    cur_i, cur_j = queue.pop()
                    if cur_i in (0, m - 1) or cur_j in (0, n - 1):
                        isClosed = False

                    for d in directions:
                        new_i = cur_i + d[0]
                        new_j = cur_j + d[1]

                        if (0 <= new_i < m) and (0 <= new_j < n) and grid[new_i][new_j] == 0:
                            queue.append((new_i, new_j))
                            grid[new_i][new_j] = 1
                if isClosed:
                    result += 1
        return result
