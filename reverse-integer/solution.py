class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        tens_place, digit, result = 0, 0, 0
        min_num, max_num = -1 * (2 ** 31) - 1, (2 ** 31) - 1

        if x == 0:
            return 0
        tens_place = int(math.floor(math.log10(abs(x))))
        sign = -1 if x < 0 else 1
        x = x * sign
        for i in range(tens_place, -1, -1):
            digit_at_place = x if i == 0 else (x / (10 ** i))
            digit = digit_at_place % 10
            result += digit * 10 ** (tens_place - i)
        result = result * sign
        return result if not (result < min_num or result > max_num) else 0
