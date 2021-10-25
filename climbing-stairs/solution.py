class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = self.searchStairs(0, n, {})
        return result

    def searchStairs(self, i, n, visited):
        if i > n:
            return 0
        if i == n:
            return 1
        if visited.get(i):
            return visited[i]
        one_stair = self.searchStairs(i + 1, n, visited)
        two_stair = self.searchStairs(i + 2, n, visited)
        visited[i] = one_stair + two_stair
        return visited[i]
