import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        self.coin_tracker = {}
        if amount == 0:
            return 0
        coin_count = self.try_coin(coins, amount)
        return coin_count

    def try_coin(self, coins, amount):
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        if self.coin_tracker.get(amount):
            return self.coin_tracker.get(amount)
        min_int = sys.maxint
        for coin in coins:
            result = self.try_coin(coins, amount - coin)
            if result >= 0 and result < min_int:
                min_int = result + 1
        self.coin_tracker[amount] = min_int if min_int != sys.maxint else -1
        return self.coin_tracker[amount]
