import bisect
from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data_structure = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.data_structure[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        values = self.data_structure.get(key, None)
        if not values:
            return ""

        sorted_index = bisect.bisect(values, (timestamp, chr(127)))
        return values[sorted_index - 1][1] if sorted_index else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
