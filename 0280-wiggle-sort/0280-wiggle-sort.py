from heapq import heapify, heappop
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        C1: (2 heaps)
            min -> max -> 2nd min -> 2nd max -> 3rd min -> ...
            O(nlogn)
        C2: sort, then swap if not following order
        """
        # min_heap = nums[::]
        # max_heap = [-n for n in nums]
        # heapify(min_heap)
        # heapify(max_heap)
        # is_min_turn = True
        # i = 0
        # while i < len(nums):
        #     if is_min_turn:
        #         nums[i] = min_heap[0]
        #         heappop(min_heap)
        #     else:
        #         nums[i] = -max_heap[0]
        #         heappop(max_heap)
        #     is_min_turn = not is_min_turn
        #     i += 1
        """
        C2: O(n)
        loop through each idx i
            if i is odd and nums[i] < nums[i+1]:
                swap i and i+1
            if i is even and nums[i] > nums[i+1]:
                swap i and i+1
        """
        def swap(i,j):
            nonlocal nums
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        for i in range(len(nums)-1):
            if i & 1 and nums[i] < nums[i+1]: # odd
                swap(i,i+1)
            if not (i & 1) and nums[i] > nums[i+1]:
                swap(i,i+1)
                
        