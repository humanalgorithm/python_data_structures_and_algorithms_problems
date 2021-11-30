from collections import OrderedDict


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.ordered_stack = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.ordered_stack.get(key) is not None:
            value = self.ordered_stack.pop(key)
            self.ordered_stack[key] = value
        return self.ordered_stack.get(key, -1)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.ordered_stack[key] = value
        self.ordered_stack.pop(key)
        self.ordered_stack[key] = value

        if len(self.ordered_stack) > self.capacity:
            first_key = next(iter(self.ordered_stack.iterkeys()))
            self.ordered_stack.pop(first_key)
