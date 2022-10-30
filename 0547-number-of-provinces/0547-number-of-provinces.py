class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0 for _ in range(n)]
        # find() returns the root node
        def find(i):
            tmp = i
            if tmp != parent[tmp]:
                # set parent[tmp] to the root node of the path by calling recursive find()
                parent[tmp] = find(parent[tmp])
                tmp = parent[tmp]
            return tmp
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
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    union(i,j)
        provinces = set()
        for i in range(n):
            par = find(i)
            provinces.add(par)
        return len(provinces)
                