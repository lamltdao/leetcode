class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_idx = -1
        min_mdist = -1
        def get_m_dist(idx):
            nonlocal x,y
            return abs(x-points[idx][0]) + abs(y-points[idx][1])
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                if min_idx == -1:
                    min_idx = i
                    min_mdist = get_m_dist(i)
                else:
                    mdist = get_m_dist(i)
                    if mdist < min_mdist:
                        min_mdist = mdist
                        min_idx = i
        return min_idx
