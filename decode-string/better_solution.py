class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_stack, count_stack = [], []
        x, result = 0, ""

        while x < len(s):
            char = s[x]
            if char.isdigit():
                int_res = ""
                while x < len(s) and s[x].isdigit():
                    int_res += s[x]
                    x += 1
                count_stack.append(int(int_res))
                x -= 1
            elif char == '[':
                char_stack.append(result)
                result = ""
            elif char == "]":
                count = count_stack.pop()
                line = char_stack.pop()
                for i in range(0, count):
                    line += result
                result = line
            else:
                result += char
            x += 1
        return result
