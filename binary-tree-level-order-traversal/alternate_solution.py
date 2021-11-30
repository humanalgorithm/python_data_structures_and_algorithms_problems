class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack1, stack2, result = [root, "break"], [], []
        line = []
        while stack1 or stack2:
            current = stack1.pop(0) if stack1 else None
            if current == "break":
                result.append(line) if line else None
                line = []
                continue
            if current:
                line.append(current.val)
                stack2.append(current.left)
                stack2.append(current.right)
            if stack2 and not stack1:
                stack1 += stack2
                stack1.insert(0, "break")
                stack2 = []
        return result
