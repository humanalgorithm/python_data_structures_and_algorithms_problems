class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return -1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.result = max(self.result, 2 + left + right)

        return 1 + max(left, right)