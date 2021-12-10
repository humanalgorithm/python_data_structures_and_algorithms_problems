class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        curr, direction = [0, 0], [0, 1]
        new_curr, new_direction = self.run_instructions(
            [0, 1], [0, 0], instructions)
        if curr == new_curr or direction != new_direction:
            return True
        return False

    def run_instructions(self, direction, curr, instructions):
        for instruction in instructions:
            if instruction == "G":
                curr[0], curr[1] = curr[0] + direction[0], curr[1] + direction[1]
            elif instruction == "L":
                direction = self.turn_left(direction)
            elif instruction == "R":
                direction = self.turn_right(direction)
        return curr, direction

    def turn_left(self, direction):
        left = [-1 * direction[1], direction[0]]
        return left

    def turn_right(self, direction):
        right = [direction[1], -1 * direction[0]]
        return right