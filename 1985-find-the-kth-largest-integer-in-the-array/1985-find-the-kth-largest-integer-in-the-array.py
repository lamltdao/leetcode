class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_to_str = {}
        arr = []
        for n_str in nums:
            n = int(n_str)
            int_to_str[n] = n_str
            arr.append(n)
        arr.sort()
        return int_to_str[arr[-k]]