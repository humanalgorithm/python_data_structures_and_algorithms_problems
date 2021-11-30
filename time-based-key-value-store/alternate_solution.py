from collections import defaultdict


class TimeMap(object):

    def __init__(self):
        self.logs = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.logs[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        entries = self.logs.get(key, [])
        l, r = 0, len(entries) - 1
        result = ""

        while l <= r:
            m = l + (r - l) / 2
            if entries[m][1] <= timestamp:
                result = entries[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
