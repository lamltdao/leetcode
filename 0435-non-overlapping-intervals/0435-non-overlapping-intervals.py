class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        sort by start
        
        if 2 consecutive intervals overlap, choose the one with smaller end
        
        O(nlogn)
        """
        intervals.sort()
        ans = 0
        # i1 <= i2
        def is_overlap(i1, i2):
            return i1[1] > i2[0]
        # i1 <= i2
        def choose_smaller_end(i1, i2):
            return i1 if i1[1] <= i2[1] else i2
        tmp_interval = intervals[0]
        next_interval_idx = 1
        while next_interval_idx < len(intervals):
            next_interval = intervals[next_interval_idx]
            if is_overlap(tmp_interval, next_interval):
                tmp_interval = choose_smaller_end(tmp_interval, next_interval)
                ans += 1
            else:
                tmp_interval = next_interval
            next_interval_idx += 1
        return ans
                
            
