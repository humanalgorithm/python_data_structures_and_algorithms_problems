class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = self.parseString(s)
        return result

    def parseString(self, s):
        x = 0
        result = ""
        while x < len(s):
            char = s[x]
            if not char.isdigit() and not char in ["[", "]"]:
                result += str(char)
            elif char.isdigit():
                k = ""
                while x < len(s) and s[x].isdigit():
                    k += s[x]
                    x += 1
                end_index = self.findIndex(s, x)
                encoded = self.parseString(s[x + 1:end_index + 1])

                for i in range(0, int(k)):
                    result += encoded
                x = end_index
            elif char == "[":
                end_index = self.findIndex(s, x)
                parse_result = self.parseString(s[x + 1:end_index])
                result += parse_result
                x = end_index
            x += 1
        return result

    def findIndex(self, s, x):
        open_bracket = 0
        close_bracket = 0

        for i in range(x, len(s)):
            char = s[i]
            if char == "[":
                open_bracket += 1
            elif char == "]":
                close_bracket += 1
            if open_bracket > 0 and close_bracket > 0 and open_bracket == close_bracket:
                return i
        return len(s) - 1