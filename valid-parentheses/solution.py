class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for bracket in s:
            if not bracket_dict.get(bracket):
                stack.append(bracket)
            else:
                open_bracket = bracket_dict.get(bracket)
                elem = stack.pop() if stack else None
                if not elem or elem != open_bracket:
                    return False
        return True if not stack else False
