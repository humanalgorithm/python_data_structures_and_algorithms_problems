class Solution(object):
    def convertPathParens(self, paths):
        return_str = []
        for path in paths:
            temp = ""
            for entry in path:
                temp += "(" * entry[0]
                temp += ")" * entry[1]
            return_str.append(temp)
        return return_str

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        avail_open = avail_closed = n
        self.valid_parens = []
        self.getValidParens(n, avail_open, avail_closed, [])
        return self.convertPathParens(self.valid_parens)

    def getValidParens(self, n, avail_open, avail_closed, path):
        used_closed, used_open = n - avail_closed, n - avail_open
        if (used_closed) > (used_open):
            return
        if avail_open == 0 and avail_closed == 0:
            self.valid_parens.append(path)
            return
        for i in range(1, avail_open + 1):
            for j in range(1, (used_open) + i + 1):
                if i == n and j < n:
                    continue
                path_copy = [elem for elem in path]
                path_copy.append((i, j))
                self.getValidParens(n, avail_open - i, avail_closed - j, path_copy)
