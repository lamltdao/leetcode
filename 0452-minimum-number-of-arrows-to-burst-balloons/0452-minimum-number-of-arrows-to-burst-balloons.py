class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        if 2 intervals overlap, take the intersection of them
        """
        ans = 1
        points.sort()
        tmp_interval = points[0]
        next_interval_idx = 1
        n = len(points)
        # i1 <= i2
        def is_overlap(i1, i2):
            return i1[1] >= i2[0]
        def intersect(i1,i2):
            return [max(i1[0], i2[0]), min(i1[1], i2[1])]
        while next_interval_idx < n:
            if is_overlap(tmp_interval, points[next_interval_idx]):
                tmp_interval = intersect(tmp_interval, points[next_interval_idx])
            else:
                tmp_interval = points[next_interval_idx]
                ans += 1
            next_interval_idx += 1
        return ans
        