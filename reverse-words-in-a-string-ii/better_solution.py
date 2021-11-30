class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        while i > 0:
            if s[i] != " ":
                end = i
                while s[i] != " " and i >= 0:
                    i -= 1
                start = i + 1
                self.flipWord(start, end, s)
            i -= 1
        self.flipWord(0, len(s) - 1, s)

    def flipWord(self, left, right, s):
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1