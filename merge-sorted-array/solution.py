class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        """

        [4,5,6,0,0,0]
        3
        [1,2,3]

        [1,2,4,5,6,0]

        [3]

        1 2 4 5 6 3



        """

        nums1_copy = nums1[:m]
        nums1[:] = []

        m_iter = 0
        n_iter = 0

        while m_iter < m and n_iter < n:
            if nums1_copy[m_iter] == nums2[n_iter]:
                nums1.append(nums1_copy[m_iter])
                nums1.append(nums2[n_iter])
                m_iter += 1
                n_iter += 1
            elif nums1_copy[m_iter] > nums2[n_iter]:
                nums1.append(nums2[n_iter])
                n_iter += 1
            elif nums1_copy[m_iter] < nums2[n_iter]:
                nums1.append(nums1_copy[m_iter])
                m_iter += 1

        while m_iter < m:
            nums1.append(nums1_copy[m_iter])
            m_iter += 1
        while n_iter < n:
            nums1.append(nums2[n_iter])
            n_iter += 1
