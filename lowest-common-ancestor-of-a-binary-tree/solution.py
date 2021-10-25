# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = []
        node = root
        parent_dict = {}

        while node:
            if node.left and node.val != None:
                stack = [node.left] + stack
                parent_dict[node.left.val] = node
            if node.right and node.val != None:
                stack = [node.right] + stack
                parent_dict[node.right.val] = node
            if stack:
                node = stack.pop()
            else:
                break

        parent_list_p = self.build_parent_list(p, parent_dict)
        parent_list_q = self.build_parent_list(q, parent_dict)

        for element in parent_list_p:
            if element.val in [node.val for node in parent_list_q]:
                return element

    def build_parent_list(self, element, parent_dict):
        current = parent = element
        parent_list = [element]
        while parent:
            parent = parent_dict.get(current.val)
            current = parent
            if parent:
                parent_list.append(parent)
        return parent_list
