
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        nodes_made = {None: None}
        node = head
        head_id = id(head)
        while node:
            new_random = id(node.random) if node.random is not None else None
            new_next = id(node.next) if node.next is not None else None
            new_node = Node(x=node.val, next=new_next, random=new_random)
            nodes_made[id(node)] = new_node
            node = node.next

        for key, val in nodes_made.items():
            if key is None:
                continue
            cur_node = nodes_made[key]
            cur_node.next = nodes_made[cur_node.next]
            cur_node.random = nodes_made[cur_node.random]

        return nodes_made[head_id]
