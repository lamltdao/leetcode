class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        basically check if there's any overlapping intervals
        """
        intervals.sort()
        # REQUIRES: intervals[i] <= intervals[j]
        def overlap(i, j):
            nonlocal intervals
            return intervals[j][0] < intervals[i][1]
        for i in range(len(intervals)-1):
            if overlap(i, i+1):
                return False
        return True