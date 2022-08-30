class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        def find(i):
            tmp = i
            while tmp != parent[tmp]:
                parent[tmp] = find(parent[tmp])
                tmp = parent[tmp]
            return parent[tmp]
        def union(i,j):
            par_i = find(i)
            par_j = find(j)
            if rank[par_i] > rank[par_j]:
                parent[par_j] = par_i
            elif rank[par_i] < rank[par_j]:
                parent[par_i] = par_j
            else:
                parent[par_j] = par_i
                rank[par_i] += 1
        
        for e in edges:
            v1, v2 = e[0], e[1]
            v1 -= 1
            v2 -= 1
            if find(v1) == find(v2):
                return e
            else:
                union(v1, v2)