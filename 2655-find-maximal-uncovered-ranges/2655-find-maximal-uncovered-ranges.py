class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        """
        cover 0 -> n-1
        sort ranges ascendingly O(nlogn)
        merge ranges if overlap O(n)
        difference of ranges to get uncovered ranges
        """
        
        # requires: r1 < r2 (range comparison)
        def overlap(r1, r2):
            return r1[1] >= r2[0]
        def merge(r1, r2):
            return [min(r1[0], r2[0]), max(r1[1], r2[1])]
        r = [[-1,-1]]
        r.extend(ranges)
        r.append([n,n])
        r.sort()
        merged_r = []
        i = 0
        """
        [-1,-1], [0,2], [3,3]
        """
        while i < len(r):
            j = i
            tmp_r = r[i]
            while j+1 < len(r) and overlap(tmp_r,r[j+1]):
                tmp_r = merge(tmp_r, r[j+1])
                j+=1
            merged_r.append(tmp_r[::])
            i = j+1
        ans = []
        for i in range(len(merged_r)-1):
            start_uncovered_r = merged_r[i][1]+1
            end_uncovered_r = merged_r[i+1][0]-1
            if start_uncovered_r <= end_uncovered_r:
                ans.append([start_uncovered_r, end_uncovered_r])
        return ans