class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry, num, sum_num, tens_place = 1, 0, 0, .1

        for x in range(len(digits) - 1, -1, -1):
            tens_place = int(tens_place * 10)
            sum_num = digits[x] + carry
            carry = 1 if sum_num >= 10 else 0
            this_digit = sum_num % 10
            num += this_digit * tens_place

        if carry:
            num += 1 * (tens_place * 10)
        return [int(x) for x in str(num)]
