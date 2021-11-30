class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        curr, jumps, end = 0, 0, len(nums) - 1
        while curr < end:
            jump = nums[curr]
            x = curr + 1
            jump_gains = []
            while x < len(nums) and x <= curr + jump:
                jump_gain = sys.maxint if x == end else nums[x] + x
                jump_gains.append((jump_gain, x))
                x += 1
            jump_gain = max(jump_gains, key=lambda x: x[0])
            curr = jump_gain[1]
            jumps += 1
        return jumps
