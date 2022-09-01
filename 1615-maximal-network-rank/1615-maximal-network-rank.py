class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        """
        for r in roads:
            network_ranks(i,j) = deg(i) + deg(j) - (1 if i,j in roads else 0)
        """
        deg = [0 for _ in range(n)]
        is_road = [[False for _ in range(n)] for _ in range(n)]
        for r in roads:
            v1,v2 = r[0], r[1]
            deg[v1] += 1
            deg[v2] += 1
            is_road[v1][v2] = is_road[v2][v1] = True
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                network_rank = deg[i] + deg[j]
                if is_road[i][j]:
                    network_rank -= 1
                ans = max(ans, network_rank)
        return ans