class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i_s = lambda x: x % 10
        iv_4s = lambda x: (x / 4) % 10
        v_s = lambda x: (x / 5) % 10
        ix_9s = lambda x: (x / 9) % 10
        x_s = lambda x: (x / 10) % 10
        lx_40s = lambda x: (x / 40) % 10
        l_s = lambda x: (x / 50) % 10
        cx_90s = lambda x: (x / 90) % 10
        c_s = lambda x: (x / 100) % 10
        cd_400s = lambda x: (x / 400) % 10
        d_s = lambda x: (x / 500) % 10
        cm_900s = lambda x: (x / 900) % 10
        m_s = lambda x: (x / 1000) % 10
        conversion_instructions = [
            ("M", m_s, 1000),
            ("CM", cm_900s, 900),
            ("D", d_s, 500),
            ("CD", cd_400s, 400),
            ("C", c_s, 100),
            ("XC", cx_90s, 90),
            ("L", l_s, 50),
            ("XL", lx_40s, 40),
            ("X", x_s, 10),
            ("IX", ix_9s, 9),
            ("V", v_s, 5),
            ("IV", iv_4s, 4),
            ("I", i_s, 1)
        ]

        output_str = ""
        for instruction in conversion_instructions:
            value = instruction[1](num)
            num = num - (value * instruction[2])
            output_str += instruction[0] * value
        return output_str