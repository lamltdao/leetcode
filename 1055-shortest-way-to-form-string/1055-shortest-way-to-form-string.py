class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        if a char in target not in source, return -1
        
        if all chars in target also in source, result never = -1
        
        alg:
        - 2 pointers, start at 0
        - try to match as many chars in source
        """
        for c in target:
            if c not in source:
                return -1
        ans = 0
        target_ptr = 0
        while target_ptr < len(target):
            source_ptr = 0
            while source_ptr < len(source) and target_ptr < len(target):
                if source[source_ptr] == target[target_ptr]:
                    target_ptr += 1
                source_ptr += 1
            ans += 1
        return ans
                