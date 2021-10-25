class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set()
        jewel_count = 0
        for char in J:
            jewels.add(char)

        for char in S:
            if char in jewels:
                jewel_count += 1
        return jewel_count
