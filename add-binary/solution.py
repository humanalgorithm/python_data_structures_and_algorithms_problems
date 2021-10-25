class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = self.convertToPower2(a)
        b = self.convertToPower2(b)

        return_num = str(bin(a + b))
        return return_num[return_num.index("b") + 1:len(return_num)]

    def convertToPower2(self, num):
        power_2, result = 0, 0
        num = num[::-1]
        for x in range(0, len(num)):
            int_num = int(num[x])
            result = result + (int_num * 2 ** power_2)
            power_2 += 1
        return result
