class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        longest_prefix = ""
        current_index = 0
        match = True

        while match and strs:
            if current_index >= len(strs[0]):
                break
            curr_char = strs[0][current_index]
            for curr_str in strs:
                if current_index >= len(curr_str) or not curr_str[current_index] == curr_char:
                    match = False
                    break
            if match:
                longest_prefix += curr_char
            current_index += 1
        return longest_prefix
