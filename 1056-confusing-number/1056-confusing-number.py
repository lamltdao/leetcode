class Solution:
    def confusingNumber(self, n: int) -> bool:
        """
        689 => 689
        """
        rotate_able = set([0,1,6,8,9])
        digits = []
        while n > 0:
            digit = n % 10
            digits.append(digit)
            n //= 10
        l = 0
        r = len(digits)-1
        is_diff = False
        while l < r:
            if digits[l] not in rotate_able or digits[r] not in rotate_able:
                return False
            if not ((digits[l] == digits[r] and digits[l] in [0,1,8]) or (digits[l] in [6,9] and digits[r] in [6,9] and digits[l] != digits[r])):
                is_diff = True
            l += 1
            r -= 1
        if l == r:
            return digits[l] in [6,9] or (digits[l] in rotate_able and is_diff)
        return is_diff