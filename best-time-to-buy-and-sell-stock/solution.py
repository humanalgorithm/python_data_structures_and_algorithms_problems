class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_int = (0, -1)
        min_int = (0, -1)
        max_difference = 0

        buy_price = prices[0] if prices else 0
        max_sale = 0
        for x in range(1, len(prices)):
            sale = prices[x] - buy_price
            if prices[x] - buy_price < 0:
                buy_price = prices[x]
                continue

            max_sale = max(max_sale, sale)

        return max_sale
