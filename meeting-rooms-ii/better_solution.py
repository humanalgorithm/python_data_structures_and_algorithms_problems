class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        rooms, max_rooms = [], 0
        for interval in intervals:
            room_avail = None
            for room in rooms:
                meeting = room[0]
                if not min(interval[1], meeting[1]) > max(interval[0], meeting[0]):
                    room.pop()
                    room.append(interval)
                    room_avail = True
                    break
            if not room_avail:
                rooms.append([interval])
            max_rooms = max(len(rooms), max_rooms)
        return max_rooms