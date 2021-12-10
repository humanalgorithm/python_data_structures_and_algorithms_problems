class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        max_result = 0
        left_dict, right_dict = {}, {}
        for combo in [(k - x, x) for x in range(0, k + 1)]:
            l, r = combo[0], combo[1]
            left_result = self.getNumberL(l, left_dict, cardPoints)
            right_result = self.getNumberR(r, right_dict, cardPoints)
            max_result = max(max_result, left_result + right_result)
        return max_result

    def getNumberL(self, l, left_dict, cardPoints):
        if left_dict.get(l):
            return left_dict.get(l)
        if l == 0:
            return 0
        left_dict[l] = cardPoints[l - 1] + self.getNumberL(l - 1, left_dict, cardPoints)
        return left_dict[l]

    def getNumberR(self, r, right_dict, cardPoints):
        if right_dict.get(r):
            return right_dict.get(r)
        if r == 0:
            return 0
        right_dict[r] = cardPoints[len(cardPoints) - r] + self.getNumberR(r - 1, right_dict, cardPoints)
        return right_dict[r]