class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        r, b, g

        cost[house_idx][color_idx]: cost of paiting house house_idx using color color_idx
        
        dp[i][color_idx]: min cost to paint all houses up to idx i, with ith house colored color_idx
        
        """
        INF = 100000000
        dp = [[INF for _ in range(3)] for _ in range(len(costs))]
        prev = [costs[0][0], costs[0][1], costs[0][2]] 
        for i in range(1, len(costs)):
            nextt = [INF,INF,INF]
            for color_idx in range(3):
                for other_color_idx in range(3):
                    if other_color_idx != color_idx:
                        nextt[color_idx] = min(nextt[color_idx], prev[other_color_idx] + costs[i][color_idx])
            prev = nextt
        return min(prev)
