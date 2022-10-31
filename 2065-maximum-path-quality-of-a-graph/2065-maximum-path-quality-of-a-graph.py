class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        """
        - # of edges(including dup) in path <= 10
        - each node has <= 4 edges connected to it
        => Time: O(4^10)
        Space: O(V+2E) to store the graph
        """
        ans = 0
        n = len(values)
        graph = [[] for _ in range(n)]
        for e in edges:
            u,v,w = e[0], e[1], e[2]
            graph[u].append((v,w))
            graph[v].append((u,w))
        def bt(path, tmp_node, tmp_time, tmp_val):
            nonlocal ans, maxTime
            if tmp_node == 0:
                ans = max(ans, tmp_val)
            for next_node, w in graph[tmp_node]:
                if tmp_time + w <= maxTime:
                    if next_node not in path:
                        path[next_node] = 0
                        tmp_val += values[next_node]
                    path[next_node] += 1
                    bt(path, next_node, tmp_time+w, tmp_val)
                    path[next_node] -= 1
                    if path[next_node] == 0:
                        del path[next_node]
                        tmp_val -= values[next_node]
        bt({0: 1}, 0, 0, values[0])
        return ans