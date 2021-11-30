class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for x in range(1, len(dp)):
            for coin in coins:
                if x - coin == 0:
                    dp[x] = min(dp[x], 1)
                elif x - coin > 0:
                    dp[x] = min(dp[x-coin]+1, dp[x])

        return dp[-1] if dp[-1] <= amount else -1
