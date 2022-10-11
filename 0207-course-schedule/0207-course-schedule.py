class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        graph
        u-> v if u is a prereq of v
        
        checkCycle(graph)
        """
        # Space: O(E)
        graph = [[] for _ in range(numCourses)]
        recur = set()
        # O(V+E)
        visited = [False for _ in range(numCourses)]
        in_recur = [False for _ in range(numCourses)]
        def hasCycle(u):
            if in_recur[u]:
                return True
            in_recur[u] = True
            visited[u] = True
            for v in graph[u]:
                if not visited[v] and hasCycle(v):
                    return True
                elif in_recur[v]:
                    return True
            in_recur[u] = False
            return False
        for p in prerequisites:
            u, v = p[0], p[1]
            graph[u].append(v)
        # O(V * (V+E)) 2000 * 7000 = 14 10^6
        for i in range(numCourses):
            visited = [False for _ in range(numCourses)]
            if hasCycle(i):
                return False
        return True