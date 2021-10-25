import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        room_heap = []
        intervals = sorted(intervals, key = lambda x: x[0])
        for interval in intervals:
            start, end = interval[0], interval[1]
            room = heapq.heappop(room_heap) if room_heap else (end, [])
            reservations = room[1]
            last_reservation = reservations[-1][-1] if reservations else None
            if len(reservations) == 0 or start >= last_reservation:
                room = (end, reservations + [interval])
            else:
                heapq.heappush(room_heap, (end, [interval]))
            heapq.heappush(room_heap, room)
        return len(room_heap)
