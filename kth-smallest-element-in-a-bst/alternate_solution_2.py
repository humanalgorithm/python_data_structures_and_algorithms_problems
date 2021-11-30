class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        import heapq
        heap_list = []
        stack = [root]

        while stack:
            current = stack.pop(0)
            heapq.heappush(heap_list, current.val)
            stack.append(current.left) if current.left else None
            stack.append(current.right) if current.right else None

        for x in range(0, k):
            elem = heapq.heappop(heap_list)

        return elem
