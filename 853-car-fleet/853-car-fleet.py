class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(position[i], speed[i]) for i in range(len(position))]
        pos_speed.sort()
        # j = i-1, or i after j
        def intersect(i,j):
            time_reach_target_i = (target-pos_speed[i][0]) / pos_speed[i][1]
            time_reach_target_j = (target-pos_speed[j][0]) / pos_speed[j][1]
            return time_reach_target_i >= time_reach_target_j
        i = len(pos_speed)-1
        ans = 0
        while i >= 0:
            while i > 0 and intersect(i,i-1):
                pos_speed[i-1] = pos_speed[i]
                i -= 1
            ans += 1
            i -= 1

        return ans
                