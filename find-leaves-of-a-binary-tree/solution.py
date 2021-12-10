class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        visited, root_add, result = set(), False, []

        while not root_add:
            stack, level = [root], []
            while stack:
                current = stack.pop()
                if current in visited:
                    continue
                right = current.right
                left = current.left
                if (not left or left in visited) and (not right or right in visited):
                    visited.add(current)
                    level.append(current.val)
                    if current == root:
                        root_add = True
                        break
                if right and right not in visited:
                    stack.append(current.right)
                if left and left not in visited:
                    stack.append(current.left)
            result.append(level)
        return result
