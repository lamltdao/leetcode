class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [False for _ in range(n)]
        graph = [[] for _ in range(n)]
        for e in edges:
            u,v = e[0], e[1]
            graph[u].append(v)
            graph[v].append(u)
        def dfs(u):
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    dfs(v)
        dfs(source)
        return visited[destination]
        