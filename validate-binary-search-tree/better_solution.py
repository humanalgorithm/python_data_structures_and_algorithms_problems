class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        stack, prev_left = [], -sys.maxint

        while stack or root:
            while root:
                stack.insert(0, root)
                root = root.left
            current = stack.pop(0)
            if prev_left >= current.val:
                return False
            prev_left = current.val
            root = current.right
        return True
