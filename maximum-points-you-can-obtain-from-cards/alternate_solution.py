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
            left_result = self.getNumberMemo(l, left_dict, cardPoints, -1, +1)
            right_result = self.getNumberMemo(r, right_dict, cardPoints, len(cardPoints), -1)
            max_result = max(max_result, left_result + right_result)
        return max_result

    def getNumberMemo(self, index, memo_dict, cardPoints, offset, index_fnc):
        if memo_dict.get(index):
            return memo_dict.get(index)
        if index == 0:
            return 0
        memo_dict[index] = cardPoints[offset + index_fnc * index] + self.getNumberMemo(
            index - 1, memo_dict, cardPoints, offset, index_fnc)
        return memo_dict[index]