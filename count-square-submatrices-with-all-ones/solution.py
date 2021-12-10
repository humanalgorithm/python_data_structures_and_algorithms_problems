class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cache = dict()
        self.searchSquare(0, 0, matrix, cache)
        return sum(cache.values())

    def searchSquare(self, i, j, matrix, cache):
        if i >= len(matrix) or j >= len(matrix[i]):
            return 0

        if (i, j) not in cache:
            up = self.searchSquare(i + 1, j, matrix, cache)
            right = self.searchSquare(i, j + 1, matrix, cache)
            diag = self.searchSquare(i + 1, j + 1, matrix, cache)

            cache[(i, j)] = 0
            if matrix[i][j] == 1:
                cache[(i, j)] = 1 + min(up, right, diag)
        return cache[i, j]