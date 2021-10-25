class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return_string = []
        for x in range(1, n + 1):
            if x % 5 == 0 and x % 3 == 0:
                output = "FizzBuzz"
            elif x % 3 == 0:
                output = "Fizz"
            elif x % 5 == 0:
                output = "Buzz"
            else:
                output = str(x)

            return_string.append(output)

        return return_string
