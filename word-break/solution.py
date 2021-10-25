class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        self.tracker = {}
        # print wordDict
        wordDict = set(wordDict)
        return self.wordSearch(s, wordDict)

    def wordSearch(self, s, wordDict):
        if len(s) <= 0:
            return True

        if self.tracker.get(s) != None:
            return self.tracker.get(s)

        for word in wordDict:
            if s[0:len(word)] == word and self.wordSearch(s[len(word):], wordDict):
                self.tracker[s[0:len(word)]] = True
                return self.tracker[s[0:len(word)]]

        self.tracker[s] = False
        return self.tracker[s]
