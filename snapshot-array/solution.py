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
        l = 0
        r = len(self.storage[index]) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.storage[index][m][0] == snap_id + 1:
                break
            elif self.storage[index][l][0] <= snap_id + 1 <= self.storage[index][m][0]:
                r = m - 1
            elif self.storage[index][m][0] <= snap_id + 1 <= self.storage[index][r][0]:
                l = m + 1
            elif snap_id + 1 < self.storage[index][l][0]:
                m = l
                break
            elif snap_id + 1 > self.storage[index][r][0]:
                m = r + 1
                break
        return self.storage[index][m - 1][1]

