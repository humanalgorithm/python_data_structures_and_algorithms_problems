class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ast = asteroids
        stack1, stack2 = [ast[0]], ast[1:]
        collide = True
        while collide:
            collide = False
            for x in range(0, len(stack2)):
                rock1 = stack1[-1] if stack1 else None
                rock2 = stack2.pop(0)
                if rock1 is not None and rock1 > 0 and rock2 < 0:
                    rock1_val, rock2_val = abs(rock1), abs(rock2)
                    if rock1_val == rock2_val:
                        stack1.pop()
                        rock2 = None
                    elif rock1_val > rock2_val:
                        rock2 = None
                    elif rock1_val < rock2_val:
                        stack1.pop()
                    collide = True
                stack1.append(rock2) if rock2 else None
            if collide:
                stack2 = stack1
                stack1 = []

        return stack1
