class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        C1: brute force: loop from left, if at a neg, check its left, get rid of pos val if absolute val < abs val of that neg, get rid of itself if >, explode both if equal abs
        O(n^2)
        """
        n = len(asteroids)
        # exploded = [False for _ in range(n)]
        # for i in range(n):
        #     if asteroids[i] < 0 and not exploded[i]:
        #         for j in range(i-1,-1,-1):
        #             if asteroids[j] > 0 and not exploded[j]:
        #                 abs_j = abs(asteroids[j])
        #                 abs_i = abs(asteroids[i])
        #                 if abs_j < abs_i:
        #                     exploded[j] = True
        #                 elif abs_j > abs_i:
        #                     exploded[i] = True
        #                     break
        #                 else:
        #                     exploded[i] = exploded[j] = True
        #                     break
        # return [asteroids[i] for i in range(n) if not exploded[i]]
        """
        C2:
        1,-4, 10,2,-5
        use a mono stack pos to push indices of pos numbers in
        when at idx i is a neg number, pop from stack as long as stack[-1] < abs of neg
        """
        stk_pos = [] # idx
        exploded = [False for _ in range(n)]
        for i in range(n):
            if asteroids[i] < 0:
                while len(stk_pos) > 0 and asteroids[stk_pos[-1]] < -asteroids[i]:
                    idx = stk_pos.pop()
                    exploded[idx] = True
                if len(stk_pos) > 0: # asteroids[stk_pos[-1]] >= -asteroids[i]
                    if asteroids[stk_pos[-1]] == -asteroids[i]:
                        idx = stk_pos.pop()
                        exploded[idx] = True
                    exploded[i] = True
            else:
                stk_pos.append(i)
        return [asteroids[i] for i in range(n) if not exploded[i]]