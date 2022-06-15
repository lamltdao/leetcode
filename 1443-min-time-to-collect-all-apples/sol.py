import sys
sys.setrecursionlimit(100000)
class Solution:
    # return [time, hasApple]
    def dfs(self,graph, hasApple, visited, v):
        visited[v] = True
        t = 0
        h_a = hasApple[v]
        for next_v in graph[v]:
            if not visited[next_v]:
                arr = self.dfs(graph, hasApple, visited, next_v)
                time, has_a = arr
                print(time,has_a,next_v)
                if has_a:
                    t += time+2
                h_a = h_a or has_a
        return t, h_a
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for e in edges:
            f, t = e[0], e[1]
            graph[f].append(t)    
            graph[t].append(f)    
        t,_ = self.dfs(graph, hasApple, visited, 0)
        return t
