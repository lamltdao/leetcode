class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        """
        if a char in target not in source, return -1
        
        if all chars in target also in source, result never = -1
        
        alg:
        - 2 pointers, start at 0
        - try to match as many chars in source
        """
        ans = 0
        target_ptr = 0
        while target_ptr < len(target):
            source_ptr = 0
            tmp = target_ptr
            while source_ptr < len(source) and tmp < len(target):
                if source[source_ptr] == target[tmp]:
                    tmp += 1
                source_ptr += 1
            if tmp > target_ptr:
                ans += 1
                target_ptr = tmp
            else:
                return -1
        return ans
                