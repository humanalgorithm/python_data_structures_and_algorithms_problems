class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        stack, right_output = [root], []
        while stack:
            level_len, level = len(stack), []
            for x in range(0, level_len):
                current = stack.pop(0)
                if current:
                    level.append(current.val)
                    stack.append(current.left) if current.left else None
                    stack.append(current.right) if current.right else None
            right_output.append(level[-1]) if level else None
        return right_output
