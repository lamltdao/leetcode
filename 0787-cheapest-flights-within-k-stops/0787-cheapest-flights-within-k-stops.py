from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # k stops means k nodes in path excluding src and dst => k+1 stops including the dst
        """
        graph adjacency list
        bfs(src)
            q (node, num_stop)
            
        return dist[dst]
        """
        graph = [[] for _ in range(n)]
        for f in flights:
            u,v,c = f[0], f[1], f[2]
            graph[u].append((v,c))
        q = deque()
        dist = [{} for _ in range(n)] # {num_stop_to_reach: dist}
        dist[src] = {0:0}
        q.append((src, 0))
        INF = 100000
        while len(q) > 0:
            u, num_stop = q.popleft()
            if num_stop < k+1:
                for v, c in graph[u]:
                    if num_stop+1 not in dist[v]:
                        dist[v][num_stop+1] = INF
                    if dist[u][num_stop] + c < dist[v][num_stop+1]:
                        dist[v][num_stop+1] = dist[u][num_stop] + c
                        q.append((v, num_stop+1))
        if len(dist[dst]) == 0: # no route
            return -1
        min_price = min([dist[dst][ns] for ns in dist[dst].keys()])
        return min_price
                        
                