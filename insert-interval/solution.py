class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        last_start = 0
        insert_point = -1

        for x in range(0, len(intervals)):
            if newInterval[0] <= intervals[x][0]:
                insert_point = x
                break
        insert_point = len(intervals) if insert_point == -1 else insert_point
        intervals = intervals[0:insert_point] + [newInterval] + intervals[insert_point:]

        stack = []

        for interval in intervals:
            stack.append(interval)
            if len(stack) >= 2:
                i2 = stack.pop()
                i1 = stack.pop()

                if min(i2[1], i1[1]) >= max(i2[0], i1[0]):
                    min_start = min(i2[0], i1[0])
                    max_end = max(i2[1], i1[1])
                    new_interval = (min_start, max_end)
                    stack.append(new_interval)
                else:
                    stack.append(i1)
                    stack.append(i2)
        return stack
