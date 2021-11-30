class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heapq.heapify(nums)
        for x in range(0, len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
    