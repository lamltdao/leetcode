from collections import deque
class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        - find the cycle: dfs + prev[]
        """
        n = len(edges)
        cycle_nodes = set()
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            e = edges[i]
            v1, v2 = e[0], e[1]
            graph[v1].append(v2)
            graph[v2].append(v1)
        prev = [None for _ in range(n)]
        cycle_detected_at = None
        prev_cycle_detected_at = None
        def dfs(u):
            nonlocal cycle_detected_at
            nonlocal prev_cycle_detected_at
            for v in graph[u]:
                if prev[v] is None:
                    prev[v] = u
                    dfs(v)
                elif prev[u] != v: # cycle detected
                    if cycle_detected_at is None:
                        cycle_detected_at = u
                        prev_cycle_detected_at = v
                        cycle_nodes.add(v)
        dfs(0)
        tmp = cycle_detected_at
        while tmp != prev_cycle_detected_at:
            cycle_nodes.add(tmp)
            tmp = prev[tmp]
        # find distance. Use bfs for each node in cycle
        INF = 10**5+1
        dist = [INF for _ in range(n)]
        for u in cycle_nodes:
            dist[u] = 0
        def bfs(u):
            q = deque()
            q.append(u)
            while len(q) > 0:
                cur_node = q.popleft()
                for v in graph[cur_node]:
                    if dist[cur_node] + 1 < dist[v]:
                        dist[v] = dist[cur_node]+1
                        q.append(v)
        for u in cycle_nodes:
            bfs(u)
        return dist
            
                
            
            