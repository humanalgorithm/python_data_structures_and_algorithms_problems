class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        row, col = 0, 0
        string_matrix = {}
        char_iter = 0
        for i in range(0, numRows):
            string_matrix[i] = {}

        while char_iter < len(s):
            row = 0
            while row < numRows and char_iter < len(s):
                # print "about to print char {} len {}".format(char_iter, len(s))
                # print "char {}".format(s[char_iter])
                string_matrix[row][col] = s[char_iter]
                char_iter += 1
                if row + 1 == numRows:
                    break
                row += 1

            row -= 1
            col += 1
            while row >= 1 and char_iter < len(s):
                string_matrix[row][col] = s[char_iter]
                col += 1
                char_iter += 1
                if row - 1 < 1:
                    break
                row -= 1

        print_str = ""
        for row in sorted(string_matrix.keys()):
            for col in sorted(string_matrix[row].keys()):
                print_str += string_matrix[row][col]
        return print_str
