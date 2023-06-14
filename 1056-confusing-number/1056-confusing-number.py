class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        C1: build an array of digits and check every "mirror" pair. O(n + log_10(n))
        """
        # rotate_able = set([0,1,6,8,9])
        # digits = []
        # while n > 0:
        #     digit = n % 10
        #     digits.append(digit)
        #     n //= 10
        # l = 0
        # r = len(digits)-1
        # is_diff = False
        # while l < r:
        #     if digits[l] not in rotate_able or digits[r] not in rotate_able:
        #         return False
        #     if not 
        #         ((digits[l] == digits[r] and digits[l] in [0,1,8])
        #          or
        #          (digits[l] in [6,9] and digits[r] in [6,9] and digits[l] != digits[r])
        #         ):
        #         is_diff = True
        #     l += 1
        #     r -= 1
        # if l == r:
        #     return digits[l] in [6,9] or (digits[l] in rotate_able and is_diff)
        # return is_diff
        """
        C2: invert n and compare. O(log_10(n))
        """
        m = {
            0:0,
            1:1,
            6:9,
            8:8,
            9:6
        }
        invert_n = 0
        tmp = n
        while tmp > 0:
            digit = tmp % 10
            if digit not in m:
                return False
            invert_n = invert_n * 10 + m[digit]
            tmp //= 10
        return n != invert_n