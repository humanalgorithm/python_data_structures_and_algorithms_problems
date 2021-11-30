class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        max_num = 0
        stack = [root]
        while stack:
            root = stack.pop()
            left_max = self.dfs(root.left) if root.left else 0
            right_max = self.dfs(root.right) if root.right else 0
            max_num = max(max_num, left_max + right_max)
            stack.append(root.right) if root.right else None
            stack.append(root.left) if root.left else None
        return max_num

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        return 1 + max(left, right)
