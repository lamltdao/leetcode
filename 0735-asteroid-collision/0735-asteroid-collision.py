class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        2,3,-5,10,2,-5,-8
        
        neg: check its left for highest absolute positive val
        pos: check its right for highest absolute neg val
        
        brute force: loop from left, if at a neg, check its left, get rid of pos val if absolute val < abs val of that neg, get rid of itself if >, explode both if equal abs
        O(n^2)
        """
        n = len(asteroids)
        exploded = [False for _ in range(n)]
        for i in range(n):
            if asteroids[i] < 0 and not exploded[i]:
                for j in range(i-1,-1,-1):
                    if asteroids[j] > 0 and not exploded[j]:
                        abs_j = abs(asteroids[j])
                        abs_i = abs(asteroids[i])
                        if abs_j < abs_i:
                            exploded[j] = True
                        elif abs_j > abs_i:
                            exploded[i] = True
                            break
                        else:
                            exploded[i] = exploded[j] = True
                            break
        return [asteroids[i] for i in range(n) if not exploded[i]]