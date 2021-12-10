class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ast = asteroids
        stack = []
        for x in range(0, len(ast)):
            if stack == [] or ast[x] > 0:
                stack.append(ast[x])
            else:
                while True:
                    rock1 = abs(stack[-1])
                    rock2 = abs(ast[x])
                    if stack[-1] < 0:
                        stack.append(ast[x])
                        break
                    elif rock1 == rock2:
                        stack.pop()
                        break
                    elif rock1 > rock2:
                        break
                    elif rock2 > rock1:
                        stack.pop()
                        if stack == []:
                            stack.append(ast[x])
                            break
        return stack