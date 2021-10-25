class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start, end = 0, 0
        while end <= len(s):
            if end == len(s) or s[end] == " ":
                self.reverse_string(s, start, end - 1)
                start = end + 1
            end += 1
        L, R = 0, len(s) - 1
        self.reverse_string(s, L, R)

    def reverse_string(self, s, L, R):
        while L < R:
            temp = s[L]
            s[L] = s[R]
            s[R] = temp
            L += 1
            R -= 1
