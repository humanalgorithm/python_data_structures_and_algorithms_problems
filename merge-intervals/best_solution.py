class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x: x[0])
        overlap_track, last_overlap = [], False

        current_interval = intervals.pop(0)
        overlap_track.append(current_interval)

        for interval in intervals:
            current_end = current_interval[1]
            next_begin = interval[0]
            next_end = interval[1]
            if current_end >= next_begin:
                overlap_track[-1][1] = max(current_end, next_end)
                current_interval = overlap_track[-1]
            else:
                current_interval = interval
                overlap_track.append(interval)
        return overlap_track
