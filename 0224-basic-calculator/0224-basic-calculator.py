class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        cur_res = 0 # current result
        cur_num = 0 # current number
        sign = 1 # sign + or - before cur
        for c in s:
            if c.isdigit():
                cur_num = cur_num*10 + int(c)
            elif c in "+-":
                cur_res += cur_num*sign
                cur_num = 0
                if c == "+":
                    sign = 1
                else:
                    sign = -1
            elif c == "(":
                # so that later when popped, know what to do
                stk.append(cur_res)
                stk.append(sign)
                cur_res = 0
                cur_num = 0
                sign = 1
            elif c == ")":
                cur_res += cur_num * sign
                s = stk.pop()
                res = stk.pop()
                cur_res = res + cur_res * s
                cur_num = 0
        return cur_res + cur_num * sign # could be cur at the end not evaluated