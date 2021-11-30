import random


class RandomizedSet(object):

    def __init__(self):
        self.map_index = dict()
        self.list_store = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.map_index.get(val) is not None:
            return False
        else:
            self.list_store.append(val)
            self.map_index[val] = len(self.list_store) - 1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.map_index.get(val) is not None:
            self.swap_list_store(val)

            self.list_store.pop()
            del self.map_index[val]
            return True
        return False

    def swap_list_store(self, val):
        curr_index = self.map_index.get(val)
        last_elem = self.list_store[len(self.list_store) - 1]
        self.list_store[curr_index] = last_elem
        self.map_index[last_elem] = curr_index

    def getRandom(self):
        """
        :rtype: int
        """
        rand = random.randrange(0, len(self.list_store))
        return self.list_store[rand]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()