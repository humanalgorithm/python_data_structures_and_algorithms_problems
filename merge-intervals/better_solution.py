class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        overlap_track, last_overlap = [], False

        while intervals:
            i1 = intervals.pop(0)
            i2 = intervals.pop(0) if intervals else []

            if self.isOverlap(i1, i2):
                overlap = [min(i1[0], i2[0]), max(i1[1], i2[1])]
                intervals = [overlap] + intervals
            else:
                overlap_track.append(i1)
                intervals = [i2] + intervals if i2 else []
        return overlap_track

    def isOverlap(self, i1, i2):
        if not i2:
            return False
        start, end = 0, 1
        max_start = max(i1[start], i2[start])
        min_end = min(i1[end], i2[end])
        if max_start <= min_end:
            return True
        return False