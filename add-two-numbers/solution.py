class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head_node, prev_node = None, None
        val, next_str = "val", "next"

        while l1 or l2 or carry:
            new_node = ListNode(0)
            head_node = new_node if not head_node else head_node
            if prev_node:
                prev_node.next = new_node
            addition_result = (getattr(l1, val, 0) + getattr(l2, val, 0) + carry)
            carry = 0 if addition_result < 10 else 1
            new_node.val = addition_result % 10
            l1, l2 = getattr(l1, next_str, None), getattr(l2, next_str, None)
            prev_node = new_node

        return head_node


