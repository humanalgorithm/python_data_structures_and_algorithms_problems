class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        node, counter = head, 0

        while node:
            counter+=1
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return None