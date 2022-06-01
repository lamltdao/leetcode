class Solution:
    def myAtoi(self, s: str) -> int:
        def rounding(num):
            minn = -2**31
            maxx = 2**31 - 1
            if num < minn:
                return minn
            if num > maxx:
                return maxx
            return num
        num_str = ''
        num_found = False
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i] == '+' or s[i] == '-' or s[i].isdigit():
                num_str += s[i]
                for j in range(i+1, len(s)):
                    if not s[j].isdigit():
                        break
                    num_str += s[j]
                break
            return 0
        if len(num_str) == 0:
            return 0
        elif num_str[0] == '+' or num_str[0] == '-':
            if len(num_str) == 1: # no digits
                return 0
            num = int(num_str[1:])
            num = num if num_str[0] == '+' else -num
            return rounding(num)
        else:
            return rounding(int(num_str))
