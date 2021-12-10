class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in pair[::-1]:
            car_arrival = float((target - p) / s)
            stack.append(car_arrival)
            if len(stack) >= 2 and stack[-1] < stack[-2]:
                stack.pop()
        return len(stack)