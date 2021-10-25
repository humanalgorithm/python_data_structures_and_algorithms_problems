class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for index, char in enumerate(haystack):
            if haystack[index] == needle[0]:
                if index + len(needle)-1 >= len(haystack):
                    break
                elif hash(haystack[index: index+len(needle)]) == hash(needle):
                        return index
        return -1
