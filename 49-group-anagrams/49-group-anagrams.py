class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = ["".join(sorted(w)) for w in strs]
        d = {}
        for i in range(len(sorted_str)):
            if sorted_str[i] not in d:
                d[sorted_str[i]] = [strs[i]]
            else:
                d[sorted_str[i]].append(strs[i])
        result = []
        for v in d.values():
            result.append(v)
        return result
            