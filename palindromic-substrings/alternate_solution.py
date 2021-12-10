class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def countPali(l, r, res):
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                else:
                    break
                l -= 1
                r += 1
            return res

        res = 0
        for i in range(0, len(s)):
            l = r = i
            res = countPali(l, r, res)

            l, r = i, i + 1
            res = countPali(l, r, res)

        return res
