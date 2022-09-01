class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        loop through string colors, if encounter 2 (or more) consecutive chars, remove all but leaves the one with the MOST neededTime
        """
        i = 0
        n = len(colors)
        ans = 0
        while i < n-1:
            if colors[i] == colors[i+1]:
                j = i+1
                summ_needed_time = neededTime[i]
                maxNeededTime = neededTime[i]
                while j < n and colors[j] == colors[i]:
                    summ_needed_time += neededTime[j]
                    maxNeededTime = max(maxNeededTime, neededTime[j])
                    j += 1
                ans += summ_needed_time - maxNeededTime
                i = j
            else:
                i += 1
        return ans