class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open_used, close_used, output = 0, 0, ""
        self.solution_set = []
        self.useParens(open_used, close_used, output, n)
        return self.solution_set

    def useParens(self, open_used, close_used, output, n):
        if open_used < n:
            self.useParens(open_used + 1, close_used, output + "(", n)
        if close_used < open_used:
            self.useParens(open_used, close_used + 1, output + ")", n)
        if open_used == close_used == n:
            self.solution_set.append(output)
