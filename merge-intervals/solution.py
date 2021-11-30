class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        i, j, removed_element = 0, 1, -1
        while i < len(intervals) - 1:
            while j < len(intervals):
                if intervals[j][0] > intervals[i][1]:
                    break
                elif intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][0]:
                    latest_end = intervals[i][1] if intervals[i][1] > intervals[j][1] else intervals[j][1]
                    intervals[j] = [intervals[i][0], latest_end]
                    intervals.remove(intervals[i])
                    removed_element = i
                    break
                j += 1
            if removed_element >= 0:
                i = removed_element
                removed_element = -1
            else:
                i += 1
            j = i + 1 if j == i else j
        return intervals

