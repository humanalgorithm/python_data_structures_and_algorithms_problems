# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        node = head
        first = True
        prev = None
        while node:
            forward_node = node.next
            node.next = prev
            prev = node
            node = forward_node
        return prev
