class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        result = []
        q = deque()
        q.append(root)

        while q:
            q_len  = len(q)
            level = []
            for x in range(0, q_len):
                node = q.popleft()
                if node:
                    q.append(node.left) if node.left else None
                    q.append(node.right) if node.right else None
                    level.append(node.val)
            result.append(level) if level else None
        return result
