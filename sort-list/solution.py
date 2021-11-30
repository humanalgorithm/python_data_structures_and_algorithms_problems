class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        import heapq
        node, stack = head, []

        while node:
            heapq.heappush(stack, (-1 * node.val, node))
            node = node.next

        stack2, cur = [], None

        for x in range(len(stack) - 1, -1, -1):
            prev = stack2.pop() if stack2 else None
            cur = heapq.heappop(stack)[1]
            stack2.append(cur)
            cur.next = prev
        return cur
