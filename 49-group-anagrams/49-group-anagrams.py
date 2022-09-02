class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            alp = [0 for _ in range(26)]
            for c in s:
                alp[ord(c) - ord('a')] += 1
            t = tuple(alp)
            if t not in d:
                d[t] = []
            d[t].append(s)
        result = []
        for v in d.values():
            result.append(v)
        return result
            