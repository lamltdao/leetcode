class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # do binary search on array of smaller size
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        l1 = 0
        r1 = len(nums1)-1
        total_length = len(nums1) + len(nums2)
        half_size_merged = total_length // 2
        INF = 10**6+1
        # binary search on first arr
        while True:
            m1 = (l1 + r1) // 2
            m2 = half_size_merged - (m1+1) - 1
            left_1 = nums1[m1] if m1 >= 0 and m1 < len(nums1) else -INF
            left_2 = nums2[m2] if m2 >= 0 and m2 < len(nums2) else -INF
            right_1 = nums1[m1+1] if m1+1 < len(nums1) and m1+1 >= 0 else INF
            right_2 = nums2[m2+1] if m2+1 < len(nums2) and m2+1 >= 0 else INF
            if left_1 <= right_2 and left_2 <= right_1:
                return min(right_1, right_2) if half_size_merged * 2 < total_length else (max(left_1, left_2) + min(right_1, right_2)) / 2
            elif left_1 >= right_2:
                r1 = m1-1
            else:
                l1 = m1+1
        return None
                
            
            