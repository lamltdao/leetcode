from heapq import heapify, heappush, heappop
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        """
        In 2D, boundary is max left and max right
        In 3D, boundary is min height of a whole region 
        Time: O(mn*log(mn))
        Space: O(mn)
        """
        regions = []
        heapify(regions)
        min_h = 100000
        # push all cells in edge
        nrow = len(heightMap)
        ncol = len(heightMap[0])
        visited = [[False for _ in range(ncol)] for _ in range(nrow)]
        for r in range(nrow):
            heappush(regions, (heightMap[r][0], r, 0, True))
            heappush(regions, (heightMap[r][ncol-1], r, ncol-1, True))
            visited[r][0] = visited[r][ncol-1] = True
        for c in range(ncol):
            heappush(regions, (heightMap[0][c], 0, c, True))
            heappush(regions, (heightMap[nrow-1][c], nrow-1, c, True))
            visited[0][c] = visited[nrow-1][c] = True
        ans = 0
        min_h_region = None
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        
        while len(regions) > 0:
            h, r, c, is_region = heappop(regions)
            if is_region:
                min_h_region = h
            for d in dirs:
                nr = r + d[0]
                nc = c + d[1]
                if 0 <= nr < nrow and 0 <= nc < ncol and not visited[nr][nc]:
                    visited[nr][nc] = True
                    if heightMap[nr][nc] < min_h_region:
                        ans += max(0, min_h_region - heightMap[nr][nc])
                        heappush(regions, (heightMap[nr][nc],nr,nc, False))
                    else:
                        heappush(regions, (heightMap[nr][nc],nr,nc, True))
        return ans
            
            