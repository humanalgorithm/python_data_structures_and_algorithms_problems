# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        self.tracker = {}
        self.searchLinkedList(head, 1)
        new_head = self.removeNodeAtN(n)
        return self.tracker.get(new_head, ListNode(""))

    def searchLinkedList(self, node, i):
        if node:
            self.tracker[i] = node
        else:
            return
        self.searchLinkedList(node.next, i + 1)

    def removeNodeAtN(self, n):
        length_of_list = self.tracker.keys()[-1]
        node_remove = (length_of_list + 1) - n
        if node_remove == 1:
            del self.tracker[1]
        else:
            self.tracker[node_remove - 1].next = self.tracker.get(node_remove + 1, None)
        return self.tracker.keys()[0] if self.tracker.keys() else -1