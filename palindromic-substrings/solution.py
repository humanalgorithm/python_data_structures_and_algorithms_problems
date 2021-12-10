class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = 0
        palindromes = 0
        while window < len(s):
            counter = 0
            curr = s[counter:counter + window + 1]
            while counter + window < len(s):
                if curr == curr[::-1]:
                    palindromes += 1
                counter += 1

                if counter + window < len(s):
                    curr = curr[1:]
                    curr += s[counter + window]
            window += 1
        return palindromes