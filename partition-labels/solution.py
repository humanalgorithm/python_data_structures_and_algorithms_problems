class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        from collections import defaultdict
        char_dict = defaultdict(int)

        for x in range(0, len(s)):
            char_dict[s[x]] +=1

        l, r = 0, 0
        result, chars_used = [], set()
        while l < len(s):
            partition = []
            while r < len(s):
                curr = s[r]
                partition.append(curr)
                chars_used.add(curr)
                char_dict[curr] -=1
                if char_dict[curr] == 0:
                    chars_used.remove(curr)
                if chars_used == set():
                    r+=1
                    break
                r+=1
            result.append(len(partition))
            l = r
        return result