class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_nums = {}

        counter = 0
        """
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                del nums[i+1]
        print nums
        """
        num_length = len(nums)
        while counter <= num_length - 2:
            # print counter
            if nums[counter] == nums[counter + 1]:
                del nums[counter + 1]
                counter -= 1
            num_length = len(nums)
            # print "counter {}  num length {}".format(counter,  num_length-1)
            counter += 1
