import bisect
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort()
        #list[ [attk_val, [def vals]] ]
        sorted_grouped_props = []
        i = 0
        while i < len(properties):
            j = i
            group = [properties[i][0], []]
            while j < len(properties) and properties[j][0] == properties[i][0]:
                group[1].append(properties[j][1])
                j += 1
            sorted_grouped_props.append(group)
            i = j
        dp_r = [None for _ in sorted_grouped_props]
        dp_r[-1] = len(sorted_grouped_props)-1
        tmp_max_def = sorted_grouped_props[-1][1][-1]
        """
        dp_r[i]: idx of the highest defense from [i+1..end]
        
        """
        for i in range(len(sorted_grouped_props)-2,-1,-1):
            dp_r[i] = dp_r[i+1]
            if sorted_grouped_props[i+1][1][-1] > tmp_max_def:
                tmp_max_def = sorted_grouped_props[i+1][1][-1]
                dp_r[i] = i+1
        ans = 0
        for i in range(len(dp_r)):
            if dp_r[i] != i:
                ans += bisect.bisect_left(sorted_grouped_props[i][1], sorted_grouped_props[dp_r[i]][1][-1])
        return ans
                    