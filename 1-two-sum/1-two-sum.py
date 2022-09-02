class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        dic {val: [indices]}
        for val in dic:
            if target-val in dic:
                if val == target-val and len(d[val]) >= 2:
                    return []
        """
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = []
            d[nums[i]].append(i)
        for num in d.keys():
            if target-num in d:
                if num == target-num and len(d[num]) >= 2:
                    return [d[num][0], d[num][1]]
                elif num != target-num:
                    return [d[num][0], d[target-num][0]]
        return []