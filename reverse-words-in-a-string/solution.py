class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        split = s.split()
        print(split)
        printout = ""
        for x in range(len(split) - 1, -1, -1):
            printout += " " + split[x]
        printout = printout[1:len(printout)]
        return printout
