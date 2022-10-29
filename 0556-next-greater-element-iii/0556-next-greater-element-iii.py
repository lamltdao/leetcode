import bisect

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        14321
        4(ptr) is greater than its right
        loop at right of 4 for digit > ptr-1 and smallest. can use binary search => idx
        swap idx with ptr-1
        reverse from ptr
        """
        # extract digits from n
        digits = []
        while n > 0:
            digits.append(n % 10)
            n //= 10
        digits.reverse()
        ans = []
        ptr = len(digits)-1
        while ptr-1 >= 0 and digits[ptr] <= digits[ptr-1]:
            ptr -= 1
        # digits are in descending order
        if not (ptr-1) >= 0:
            return -1
        prev_ptr_digit = digits[ptr-1]
        # reverse from ptr
        digits[ptr:] = digits[ptr:][::-1]
        idx = bisect.bisect_right(digits, prev_ptr_digit, ptr, len(digits))
        # can't find digit to replace
        if idx >= len(digits) or idx < 0:
            return -1
        digits[idx], digits[ptr-1] = digits[ptr-1], digits[idx]
        new_n = 0
        mul = 1
        LIM = 2**31-1
        for i in range(len(digits)-1,-1,-1):
            added = digits[i] * mul
            if new_n + added > LIM:
                return -1
            new_n += added
            mul *= 10
        return new_n
                
                
                
                    
            
        