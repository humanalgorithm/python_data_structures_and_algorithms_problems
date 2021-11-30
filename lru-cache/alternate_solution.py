class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node("Head", None)
        self.tail = Node("Tail", None)
        self.capacity = capacity
        self.node_map = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev

        next_node.prev = prev_node
        prev_node.next = next_node

    def add(self, node, head):
        current_first_node = self.head.next
        node.next = current_first_node
        current_first_node.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        result = -1
        node = self.node_map.get(key)
        if node is not None:
            result = node.val
            self.remove(node)
            self.add(node, self.head)
        return result

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.node_map.get(key)
        if node is not None:
            self.remove(node)
            node.val = value
            self.add(node, self.head)
        else:
            if len(self.node_map) == self.capacity:
                del self.node_map[self.tail.prev.key]
                self.remove(self.tail.prev)
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.add(new_node, self.head)