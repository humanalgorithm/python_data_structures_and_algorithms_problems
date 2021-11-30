class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        output = []
        self.kth_value = 0
        self.traverseTree(root, k, output)
        return self.kth_value

    def traverseTree(self, root, k, output):
        stack = [root]

        while stack:
            current = stack.pop()
            if current.left:
                self.traverseTree(current.left, k, output)

            output.append(current.val)
            if len(output) == k:
                self.kth_value = output[-1]
                return
            stack.append(current.right) if current.right else None
