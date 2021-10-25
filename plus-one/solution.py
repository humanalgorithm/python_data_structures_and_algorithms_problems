class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        carry = 0
        addition = 0
        for x in range(len(digits) - 1, -1, -1):
            if x == len(digits) - 1:
                addition = 1
            elif carry:
                addition = carry

            if addition:
                result = digits[x] + addition
                digits[x] = result - 10 if result > 9 else result
                # print "result {}".format(result)
                if result > 9:
                    carry = 1
                else:
                    carry = 0
                addition = 0
        if carry == 1:
            digits = [1] + digits
        return digits

