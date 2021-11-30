class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        char_counter, pixel, lines = 0, 0, []
        line = ""

        while char_counter < len(S):
            char = S[char_counter]
            char_num = ord(char) - ord('a')
            width = widths[char_num]

            if pixel + width <= 100:
                line += char
            else:
                lines.append(line)
                line = char
                pixel = 0
            pixel += width
            char_counter += 1

        lines.append(line)
        return [len(lines), pixel]
