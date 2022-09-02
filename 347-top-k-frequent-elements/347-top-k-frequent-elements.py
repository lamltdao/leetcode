class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = 1 if num not in d else d[num] + 1
        count_to_vals = [[] for _ in range(len(nums)+1)]
        for num in d.keys():
            count_to_vals[d[num]].append(num)
        ans = []
        num_val_added = k
        for cnt in range(len(count_to_vals)-1, -1, -1):
            if len(ans) == k:
                break
            if len(count_to_vals[cnt]) > 0:
                for i in range(min(num_val_added, len(count_to_vals[cnt]))):
                    ans.append(count_to_vals[cnt][i])
                num_val_added -= min(num_val_added, len(count_to_vals[cnt]))
        return ans