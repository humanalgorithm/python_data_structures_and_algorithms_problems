# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count, max_distance, self.visited, = 0, 0, {}
        if not root:
            return 0

        stack = [root]
        while stack:
            left, right = 0, 0
            node = stack.pop()
            if node.right:
                left = self.getDepth(node.right)
                stack.append(node.right)
            if node.left:
                right = self.getDepth(node.left)
                stack.append(node.left)
            max_distance = max(max_distance, left + right)
            count += 1
        return max_distance

    def getDepth(self, node):
        if self.visited.get(id(node)):
            return self.visited[id(node)]

        if not node.left and not node.right:
            return 1

        right_height, left_height = 0, 0
        if node.right:
            right_height = 1 + self.getDepth(node.right)

        if node.left:
            left_height = 1 + self.getDepth(node.left)

        self.visited[id(node)] = max(right_height, left_height)
        return self.visited[id(node)]
