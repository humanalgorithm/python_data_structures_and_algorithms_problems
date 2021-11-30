class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, s = [], str(s)

        for x in range(0, len(s)):
            char = s[x]
            if char in ["(", ")"]:
                stack.append((str(char), x))
            if char == ")":
                first = stack.pop()
                second = stack.pop() if stack else None
                if first and not second:
                    stack.append(first)
                elif second and second[0] != "(":
                    stack.append(second)
                    stack.append(first)
        counter = 0
        for skip_entry in stack:
            skip_index = skip_entry[1]
            s = s[:skip_index+counter]  + s[skip_index+counter+1:]
            counter-=1
        return s
