import functools

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        def comparator(p_prev, p_next):
            if p_prev[0] != p_next[0]:
                return 1 if p_prev[0] > p_next[0] else -1
            else:
                return 1 if p_prev[1] < p_next[1] else -1
        properties.sort(key=functools.cmp_to_key(comparator))
        maxDef = properties[-1][1]
        ans = 0
        for i in range(len(properties)-1, -1, -1):
            if properties[i][1] < maxDef:
                ans += 1
            maxDef = max(maxDef, properties[i][1])
        return ans