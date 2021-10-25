# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if not root:
            return True

        stack.append(root)
        valid, left_valid, right_valid = True, True, True
        while stack:
            node = stack.pop()
            if node.right and node.right.val != None:
                right_valid = self.checkIsSubtreeGreater(node.right, node.val)
                stack.append(node.right)
            if node.left and node.left.val != None:
                left_valid = self.checkIsSubtreeLesser(node.left, node.val)
                stack.append(node.left)

            if left_valid == False or right_valid == False:
                return False
        return valid

    def checkIsSubtreeLesser(self, node, value):
        stack = [node]
        valid = True
        while stack:
            node = stack.pop()
            if node.val >= value:
                valid = False

            if node.right and node.right.val != None:
                stack.append(node.right)
            if node.left and node.left.val != None:
                stack.append(node.left)
        return valid

    def checkIsSubtreeGreater(self, node, value):
        stack = [node]
        valid = True
        while stack:
            node = stack.pop()
            if node.val <= value:
                valid = False
            if node.right and node.right.val != None:
                stack.append(node.right)
            if node.left and node.left.val != None:
                stack.append(node.left)
        return valid
