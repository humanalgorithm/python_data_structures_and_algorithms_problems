class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        close_brackets = [")", "]", "}"]
        bracket_dict = {
            ")": {"inverse": "("},
            "]": {"inverse": "["},
            "}": {"inverse": "{"},
            "(": {"inverse": ")"},
            "[": {"inverse": "]"},
            "{": {"inverse": "}"}
        }

        for char in s:
            stack.append(char)
            previous_char, char_count = "", 0
            while len(stack) >= 1 and char in close_brackets:
                popped = stack.pop()
                char_count += 1
                if popped == bracket_dict.get(char)['inverse']:
                    break
                elif previous_char and popped != bracket_dict.get(previous_char)['inverse']:
                    return False
                previous_char = popped
            if char_count % 2 != 0:
                return False
        return not stack
