class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        left = [0] * n
        right = [0] * n
        dp = points[0]

        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    left[j] = dp[j]
                else:
                    left[j] = max(left[j - 1] - 1, dp[j])

            for x in range(n - 1, -1, -1):
                if x == n - 1:
                    right[x] = dp[x]
                else:
                    right[x] = max(right[x + 1] - 1, dp[x])

            for y in range(n):
                dp[y] = points[i][y] + max(left[y], right[y])

        return max(dp)
