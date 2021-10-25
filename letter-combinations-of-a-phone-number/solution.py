class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone_number_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        # print phone_number_map
        digits = str(digits)
        if digits == "":
            return []
        num_spaces_int = 1
        num_spaces = [len(phone_number_map.get(digit)) for digit in digits]
        for digit in num_spaces:
            num_spaces_int = num_spaces_int * digit
        combos = ["" for x in range(num_spaces_int)]

        for index, digit in enumerate(digits):
            letters = phone_number_map.get(digit)
            len_letters = len(letters)
            for x in range(0, num_spaces_int):
                letter = letters[x % len_letters]
                combos[x] = combos[x] + letter
            combos = sorted(combos)
        return combos

