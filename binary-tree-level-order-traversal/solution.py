class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack1, stack2, result = [root], [], []
        while stack1 or stack2:
            line = []
            while stack1:
                current = stack1.pop(0)
                if not current:
                    continue
                line.append(current.val)
                stack2.append(current.left)
                stack2.append(current.right)

            result.append(line) if line else None

            line = []
            while stack2:
                current = stack2.pop(0)
                if not current:
                    continue
                line.append(current.val)
                stack1.append(current.left)
                stack1.append(current.right)

            result.append(line) if line else None
        return result