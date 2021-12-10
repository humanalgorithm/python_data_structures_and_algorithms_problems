class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(cardPoints) - k
        window = cardPoints[r:]
        total = sum(window)
        result = total

        while r < len(cardPoints):
            total += (cardPoints[l] - cardPoints[r])
            result = max(total, result)
            r += 1
            l += 1
        return result
