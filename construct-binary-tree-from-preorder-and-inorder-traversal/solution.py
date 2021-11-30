class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # (a) Inorder (Left, Root, Right) : 4 2 5 1 3
        # (b) Preorder (Root, Left, Right) : 1 2 4 5 3
        # (c) Postorder (Left, Right, Root) : 4 5 2 3 1]

        if not preorder or not inorder:
            return None
        preorder_root = preorder[0]
        root = TreeNode(val=preorder_root)
        in_root_index = inorder.index(preorder_root)

        root.left = self.buildTree(preorder[1:in_root_index + 1], inorder[:in_root_index])
        root.right = self.buildTree(preorder[in_root_index + 1:], inorder[in_root_index + 1:])

        return root