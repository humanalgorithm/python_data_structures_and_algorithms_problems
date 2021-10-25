class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words = {}

        for word in strs:
            word_sorted = str(sorted(word))
            if not words.get(word_sorted):
                words[word_sorted] = []
            words[word_sorted].append(word)

        return [value for key, value in words.iteritems()]
