class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        ans = 0
        for n in arr:
            if n+1 in s:
                ans += 1
        return ans