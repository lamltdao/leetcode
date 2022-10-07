from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        create graph
        for each node: dfs(node) -> [time, num_node]
            if num_node == n:
                ans = min(ans, time)
        """
        graph = [[] for _ in range(n)]
        for t in times:
            u,v,w = t[0],t[1],t[2]
            u -= 1
            v -= 1
            graph[u].append((v,w))
        INF = 10**7
        ans = INF
        dist = [INF for _ in range(n)]
        def bfs(i):
            q = deque()
            q.append(i)
            dist[i] = 0
            while len(q) > 0:
                u = q.popleft()
                for v, time in graph[u]:
                    if dist[u] + time < dist[v]:
                        dist[v] = dist[u] + time
                        q.append(v)
        ans = INF
        dist = [INF for _ in range(n)]
        bfs(k-1)
        max_d = 0
        all_receive = True
        for d in dist:
            if d == INF:
                all_receive = False
                break
            max_d = max(max_d, d)
        if all_receive:
            ans = min(ans, max_d)
        return ans if ans != INF else -1
            