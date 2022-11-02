from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        length of gene = 8
        length of bank <= 10
        
        for each pair of gene in bank.extend(start):
            if gene a can be mutated into gene b:
                make an undirected edge
        bfs(start)
        return dist[end] if end in dist else -1
        Time: O(V^2 * 8 + E+V) = O(V^2), V = O(len(bank))
        Space: O(2E+V)
        """
        bank = set(bank)
        graph = {}
        bank.add(start)
        def is_mutation(g1, g2):
            num_diff = 0
            for i in range(len(g1)):
                if g1[i] != g2[i]:
                    num_diff += 1
            return num_diff == 1
        for g1 in bank:
            if g1 not in graph:
                graph[g1] = set()
            for g2 in bank:
                if g2 not in graph:
                    graph[g2] = set()
                if g1 != g2 and is_mutation(g1, g2):
                    graph[g1].add(g2)
                    graph[g2].add(g1)
        INF = 100
        dist = {k: INF for k in graph.keys()}
        dist[start] = 0
        q = deque()
        q.append(start)
        while len(q) > 0:
            g1 = q.popleft()
            for g2 in graph[g1]:
                if dist[g1] + 1 < dist[g2]:
                    dist[g2] = dist[g1]+1
                    q.append(g2)
        return dist[end] if end in dist and dist[end] != INF else -1
        