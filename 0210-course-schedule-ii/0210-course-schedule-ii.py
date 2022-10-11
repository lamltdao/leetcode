from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        q = deque()
        for p in prerequisites:
            u, v = p[0], p[1]
            graph[v].append(u)
            indeg[u] += 1
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        ans = []
        while len(q) > 0:
            u = q.popleft()
            ans.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if any(indeg): # still edges => loop
            return []
        return ans