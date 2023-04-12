class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {}
        tmp = 0
        for i in range(len(nums)):
            tmp = (tmp + nums[i]) % k
            if tmp not in d:
                d[tmp] = 0
            d[tmp] += 1
        ans = 0
        for mod, num_indices in d.items():
            if mod == 0:
                ans += num_indices
            ans += num_indices * (num_indices-1) // 2
        return ans
        