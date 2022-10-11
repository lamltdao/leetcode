from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        graph
        u-> v if u is a prereq of v
        
        checkCycle(graph)
        
        c2: topposort
        u-> v if v is a prereq of u
        """
        # Space: O(E)
        graph = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        for p in prerequisites:
            u, v = p[0], p[1]
            graph[v].append(u)
            indeg[u] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while len(q) > 0:
            u = q.popleft()
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return not any(indeg)