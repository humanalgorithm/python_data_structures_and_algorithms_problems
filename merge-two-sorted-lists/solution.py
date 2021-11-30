# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if l1 else l2
        head = l1
        while l1 and l2:
            if l1.val > l2.val:
                temp = l1.val
                l1.val = l2.val
                l2.val = temp

            if l1.val <= l2.val:
                if l1.next and l1.next.val < l2.val:
                    l1 = l1.next
                    continue
                l1_next = l1.next
                l2_next = l2.next

                l1.next = l2
                l2.next = l1_next

                l1 = l2
                l2 = l2_next
                continue

            l1 = l1.next
            l2 = l2.next

        return head
