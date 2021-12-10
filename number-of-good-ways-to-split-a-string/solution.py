class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        l = defaultdict(int)
        r = defaultdict(int)
        result = 0
        l[s[0]] += 1
        for x in range(1, len(s)):
            r[s[x]] += 1
        result = result + 1 if l.keys() == r.keys() else result

        for x in range(1, len(s)):
            l[s[x]] += 1
            r[s[x]] -= 1
            if not l[s[x]]:
                del l[s[x]]
            if not r[s[x]]:
                del r[s[x]]
            if len(l.keys()) == len(r.keys()):
                result += 1
        return result