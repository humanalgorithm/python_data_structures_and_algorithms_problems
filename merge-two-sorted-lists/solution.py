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
        node_1 = l1
        node_2 = l2
        case = True
        head = None
        first = True
        last_direction = +1
        if l1 and not l2:
            updated_node = l1
        elif l2 and not l1:
            updated_node = l2
        else:
            updated_node = None
        head = None
        while (node_1 or node_2) and case:

            node_1_forward = node_1.next if node_1 else None
            node_2_forward = node_2.next if node_2 else None
            node_1_val = node_1.val if node_1 else None
            node_2_val = node_2.val if node_2 else None

            if node_1 and node_1_val == node_2_val:
                if last_direction == +1:
                    updated_node = node_1
                    node_1.next = node_2
                    node_1 = node_1_forward
                    last_direction = -1
                else:
                    updated_node = node_2
                    node_2.next = node_1
                    node_2 = node_2_forward
                    last_direction = +1
            elif node_2 and node_2_val < node_1_val:
                updated_node = node_2
                last_direction = +1
                if node_2.next and node_2.next.val < node_1_val:
                    node_2 = node_2_forward
                else:
                    node_2.next = node_1
                    node_2 = node_2_forward
            elif node_1 and node_2_val > node_1_val:
                updated_node = node_1
                last_direction = -1
                if node_1.next and node_1.next.val < node_2.val:
                    node_1 = node_1_forward
                else:
                    node_1.next = node_2
                    node_1 = node_1_forward
            else:
                case = False
            if first == True:
                head = updated_node
                first = False

        return head
