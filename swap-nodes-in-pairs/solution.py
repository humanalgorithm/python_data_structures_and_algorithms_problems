# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev, node = None, head
        stack, swap_stack = [], []
        while node:
            stack.append(node)
            node = node.next
        while stack:
            node1 = stack.pop(0)
            node2 = stack.pop(0) if stack else None

            swap_stack.append(node2) if node2 else None
            swap_stack.append(node1)

        head = swap_stack[0]
        while swap_stack:
            node = swap_stack.pop(0)
            node.next = None
            if prev:
                prev.next = node
            prev = node
        return head
