class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete, stack, result = set(to_delete), [root], set()

        while stack:
            current = stack.pop()
            self.add_to_delete(current, to_delete, result)
            right = current.right
            if right and right.val in to_delete:
                current.right = None
            stack.append(right) if right else None

            left = current.left
            if left and left.val in to_delete:
                current.left = None
            stack.append(left) if left else None
        result.add(root) if root.val not in to_delete else None
        return result

    def add_to_delete(self, current, to_delete, result):
        if current.val in to_delete:
            if current.left and current.left.val not in to_delete:
                result.add(current.left)
            if current.right and current.right.val not in to_delete:
                result.add(current.right)


