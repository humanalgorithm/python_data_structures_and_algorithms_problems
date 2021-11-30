class Solution(object):
    class Solution(object):
        def longestPalindrome(self, s):
            """
            :type s: str
            :rtype: str
            """

            start, longest = 0, ""

            while start < len(s):
                even = self.checkPalindrome(s, start, start, start + 1, "")
                odd = self.checkPalindrome(s, start, start - 1, start + 1, s[start])
                longest = even if len(even) > len(longest) else longest
                longest = odd if len(odd) > len(longest) else longest
                start += 1
            return longest

        def checkPalindrome(self, s, start, left, right, longest):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    longest = s[left] + longest + s[right]
                    left -= 1
                    right += 1
                else:
                    break
            return longest






