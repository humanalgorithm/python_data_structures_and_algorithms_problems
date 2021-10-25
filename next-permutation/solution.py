class Solution(object):
    def nextPermutation(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        i = n - 1
        while i > 0:
            if a[i - 1] < a[i]:
                k = i
                for j in range(i, n):
                    if a[i - 1] < a[j] < a[k]:
                        k = j
                a[i - 1], a[k] = a[k], a[i - 1]
                b = sorted(a[i:])
                del a[i:]
                a.extend(b)
                return
            i -= 1
        a.sort()
