class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """
        (4*3 + 2*5 + 1* 6) // 2 = 14
        
        """
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        group_count = {} # group_num: num of nodes
        group_num = 0
        visited = [False for _ in range(n)]
        def dfs(u):
            nonlocal group_num
            visited[u] = True
            group_count[group_num] += 1
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)
        for i in range(n):
            if not visited[i]:
                group_count[group_num] = 0
                dfs(i)
                group_num += 1
        summ = 0
        count = 0
        for group_num in group_count.keys():
            count += group_count[group_num]
        for group_num in group_count.keys():
            summ += group_count[group_num] * (count -  group_count[group_num])
        return summ // 2
        