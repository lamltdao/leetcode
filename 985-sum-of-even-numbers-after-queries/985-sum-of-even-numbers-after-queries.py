class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_even = sum([n for n in nums if not (n & 1)])
        for q in queries:
            val, idx = q[0], q[1]
            if not (val & 1):
                if not (nums[idx] & 1):
                    sum_even += val
                nums[idx] += val
                ans.append(sum_even)
            else:
                if not (nums[idx] & 1):
                    sum_even -= nums[idx]
                else:
                    sum_even += nums[idx] + val
                nums[idx] += val
                ans.append(sum_even)
        return ans
            