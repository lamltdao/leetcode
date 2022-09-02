from heapq import heapify, heappop
# USING PQ IS ASYMTOTICALLY FASTER THAN SORTING
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 if num not in d else d[num] + 1
        arr = []
        for num, freq in d.items():
            arr.append((-freq,num))
        heapify(arr)
        result = []
        for i in range(k):
            _,n = heappop(arr)
            result.append(n)
        return result