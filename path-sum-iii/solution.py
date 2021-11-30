class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        def dfs(root, curr_sum, counter):
            if not root:
                return
            if curr_sum is None:
                curr_sum = 0
            if root.val + curr_sum == targetSum:
                counter[0] += 1

            dfs(root.left, curr_sum + root.val, counter)
            dfs(root.right, curr_sum + root.val, counter)

        stack = [root]
        counter = [0]
        while stack and root:
            curr = stack.pop(0)
            dfs(curr, None, counter)
            stack.append(curr.left) if curr.left else None
            stack.append(curr.right) if curr.right else None
        return counter[0]