class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        rooms = []
        
        intervals.sort(key=lambda x:x[0])   # sort by start time
        
        heapq.heappush(rooms, intervals[0][1])
        
        for i in intervals[1:]:
            
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, i[1])
        
        return len(rooms)