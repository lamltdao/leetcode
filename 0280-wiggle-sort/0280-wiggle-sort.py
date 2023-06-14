from heapq import heapify, heappop
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        min -> max -> 2nd min -> 2nd max -> 3rd min -> ...
        """
        min_heap = nums[::]
        max_heap = [-n for n in nums]
        heapify(min_heap)
        heapify(max_heap)
        is_min_turn = True
        i = 0
        while i < len(nums):
            if is_min_turn:
                nums[i] = min_heap[0]
                heappop(min_heap)
            else:
                nums[i] = -max_heap[0]
                heappop(max_heap)
            is_min_turn = not is_min_turn
            i += 1
        