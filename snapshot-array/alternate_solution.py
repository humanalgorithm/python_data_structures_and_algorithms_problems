class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.storage = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.storage and self.storage[index][-1][0] == self.snap_id:
            self.storage[index].pop()
        self.storage[index].append([self.snap_id, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        m = bisect.bisect(self.storage[index], x=[snap_id + 1])
        return self.storage[index][m - 1][1]

