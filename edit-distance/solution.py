class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        ctable = [[j] + [i for i in range(1, n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    ctable[i][j] = ctable[i - 1][j - 1]
                else:
                    ctable[i][j] = 1 + min(ctable[i - 1][j], ctable[i - 1][j - 1], ctable[i][j - 1])
        return ctable[-1][-1]

