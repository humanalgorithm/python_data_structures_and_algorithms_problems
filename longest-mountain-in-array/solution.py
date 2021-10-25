class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mtn, max_mtn, last_up, n = 1, 0, False, len(A)
        for x in range(1, n):
            if A[x] > A[x-1]:
                mtn = mtn+1 if last_up else 2
                last_up = True
            elif mtn > 1 and A[x] < A[x-1]:
                mtn +=1
                max_mtn = max_mtn if max_mtn > mtn else mtn
                last_up = False
            else:
                mtn, last_up = 1, False
        return max_mtn
