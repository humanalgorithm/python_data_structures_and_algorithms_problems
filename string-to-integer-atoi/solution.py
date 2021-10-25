class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        int_str = ""
        INT_MIN, INT_MAX = 2 ** 31 * -1, 2 ** 31 - 1
        seen_int = False
        for x in range(0, len(str)):
            if str[x] == " " and not seen_int:
                continue
            elif str[x] == "-" and not seen_int:
                sign = -1
            elif str[x] == "+" and not seen_int:
                sign = 1
            elif not str[x].isdigit():
                break
            else:
                int_str += str[x]
            seen_int = True

        int_int = int(int_str) * sign if len(int_str) > 0 else 0

        if int_int < INT_MIN:
            return INT_MIN
        elif int_int > INT_MAX:
            return INT_MAX
        else:
            return int_int