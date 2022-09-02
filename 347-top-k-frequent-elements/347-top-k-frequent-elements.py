from heapq import heapify, heappop
# USING PQ IS ASYMTOTICALLY FASTER THAN SORTING
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 if num not in d else d[num] + 1
        arr = []
        for num in d.keys():
            arr.append((-d[num], num))
        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans