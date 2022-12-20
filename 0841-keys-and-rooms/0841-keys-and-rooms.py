class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        visit 0
        """
        n = len(rooms)
        visited = [False for _ in range(n)]
        def dfs(u):
            visited[u] = True
            for v in rooms[u]:
                if not visited[v]:
                    dfs(v)
        dfs(0)
        return all(visited)