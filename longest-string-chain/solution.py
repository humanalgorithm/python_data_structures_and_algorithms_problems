class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        from collections import defaultdict
        word_dict = defaultdict(list)
        self.max_path = 0

        for word in words:
            for x in range(0, len(word)):
                new_word = word[:x] + "*" + word[x + 1:]
                word_dict[new_word].append(word)

        visited = dict()
        for key in sorted(word_dict.keys()):
            result = self.search(key, word_dict, visited)
            self.max_path = max(self.max_path, result)
            if result == len(words):
                return self.max_path
        return self.max_path

    def search(self, curr, word_dict, visited):
        if curr in visited:
            return visited[curr]
        visited[curr] = 0
        for entry in word_dict.get(curr, []):
            search_terms = [entry[:x] + "*" + entry[x:] for x in range(0, len(entry) + 1)]
            results = [1 + self.search(s, word_dict, visited) for s in search_terms]
            visited[curr] = max(max(results), visited[curr])
        return visited[curr]
