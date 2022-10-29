class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        1-2
        1-3
        2-4
        
        1-2-4
         \3
        2 coloring prob
        """
        graph = [[] for _ in range(n)]
        for d in dislikes:
            u,v = d[0], d[1]
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        colored = [None for _ in range(n)]# true-red, false-blue
        # return True if u is successfully colored
        def dfs(u, color): 
            colored[u] = color
            for v in graph[u]:
                if colored[v] is None:
                    dfs(v, not color)
                elif colored[v] == color: 
                    return False
            return True
        for i in range(n):
            if colored[i] is None:
                if not dfs(i, True):
                    return False
        return True