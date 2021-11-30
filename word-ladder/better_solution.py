from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = defaultdict(list)

        for word in wordList:
            for j in range(0, len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                wordDict[pattern].append(word)

        level, visited, q = 1, set(), [beginWord]
        visited.add(beginWord)

        while q:
            for j in range(0, len(q)):
                word = q.pop(0)
                if word == endWord:
                    return level
                for j in range(0, len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neigh in wordDict[pattern]:
                        if neigh not in visited:
                            q.append(neigh)
                            visited.add(neigh)
            level += 1
        return 0
