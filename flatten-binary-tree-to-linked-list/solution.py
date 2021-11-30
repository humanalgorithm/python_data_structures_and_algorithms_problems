class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        stack = [root] if root else []
        output = []
        self.preOrder(stack, output)

        stack = []
        prev = None
        for x in range(len(output) - 1, -1, -1):
            prev = stack.pop() if stack else None
            cur = output[x]
            cur.right = prev
            cur.left = None
            stack.append(cur)
        return root

    def preOrder(self, stack, output):
        while stack:
            current = stack.pop()
            output.append(current)
            if current.left:
                stack.append(current.left)
                self.preOrder(stack, output)
            stack.append(current.right) if current.right else None