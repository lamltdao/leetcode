from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for t in times:
            u,v,w = t[0], t[1], t[2]
            u -= 1
            v -= 1
            graph[u].append((v,w))
        INF = 100000
        dist = [INF for _ in range(n)]
        def bfs(src):
            dist[src] = 0
            q = deque()
            q.append(src)
            while len(q) > 0:
                u = q.popleft()
                for v,w in graph[u]:
                    if dist[u]+w < dist[v]:
                        dist[v] = dist[u]+w
                        q.append(v)
        bfs(k-1)
        max_dist = max(dist)
        return max_dist if max_dist != INF else -1