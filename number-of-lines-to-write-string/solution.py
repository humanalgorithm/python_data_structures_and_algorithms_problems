class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line_character_count = 0
        line_count = 1
        width_dict = {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for x in range(0, len(widths)):
            width_dict[alphabet[x]] = widths[x]

        for x in range(0, len(S)):
            width = width_dict.get(S[x])

            if line_character_count + width > 100:
                line_character_count = 0
                line_count += 1
            line_character_count += width

        return [line_count, line_character_count]
