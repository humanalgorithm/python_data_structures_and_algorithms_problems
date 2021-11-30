class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.searchWord(s, "", wordDict, set())

    def searchWord(self, s, current, wordDict, visited):
        if current in visited:
            return False
        visited.add(current)

        if (current[:len(current)] != s[:len(current)] or
                len(current) > len(s)):
            return False

        if current == s:
            return True

        for word in wordDict:
            result = self.searchWord(s, current + word, wordDict, visited)
            if result:
                return True
        return False
