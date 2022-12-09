class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        C1: Same as minCost problem => Time: O(n*k^2). Space: O(k)
        C2: O(nk)
        in each "layer", it suffices to know 2 smallest value and their corresponding idx
        """
        n = len(costs)
        k = len(costs[0])
        prev = [costs[0][i] for i in range(k)]
        def get_smallest_idx(arr):
            idx = 0
            for i in range(1, len(arr)):
                if arr[i] < arr[idx]:
                    idx = i
            return idx
        def get_second_smallest_idx(arr, smallest_idx):
            idx = None
            for i in range(len(arr)):
                if i != smallest_idx and (idx is None or arr[i] < arr[idx]):
                    idx = i
            return idx
        smallest_idx = get_smallest_idx(prev)
        second_smallest_idx = get_second_smallest_idx(prev, smallest_idx)
        INF = 10**8
        for i in range(1,n):
            nextt = [INF for _ in range(k)]
            for c_idx in range(k):
                if c_idx != smallest_idx:
                    nextt[c_idx] = min(nextt[c_idx], prev[smallest_idx] + costs[i][c_idx])
                else:
                    nextt[c_idx] = min(nextt[c_idx], prev[second_smallest_idx] + costs[i][c_idx])
            prev = nextt
            smallest_idx = get_smallest_idx(prev)
            second_smallest_idx = get_second_smallest_idx(prev, smallest_idx)
        return min(prev)