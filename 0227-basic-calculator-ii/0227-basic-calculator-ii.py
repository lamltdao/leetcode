class Solution:
    def calculate(self, s: str) -> int:
        """
        Time: O(s), Space: O(s) bc of stack
        Can optimize not using stack by keep track of prev_num => Space O(1)
        """
        numbers = set([str(i) for i in range(10)])
        operations = set(["+", "-", "*", "/"])
        prev_num = None
        ans = 0
        i = 0
        sign = 1
        prev_op = None
        while i < len(s):
            c = s[i]
            if c in numbers:
                num_str = [c]
                while i+1 < len(s) and s[i+1] in numbers:
                    num_str.append(s[i+1])
                    i += 1
                num = int(''.join(num_str))
                if prev_op is None:
                    # stk.append(sign * num)
                    prev_num = sign * num
                    ans += prev_num
                elif prev_op == "*":
                    # stk.append(stk.pop() * num)
                    ans -= prev_num
                    prev_num *= num
                    ans += prev_num
                else:
                    ans -= prev_num
                    sign = 1 if prev_num > 0 else -1
                    # stk.append(abs(n) // num * sign)
                    prev_num = abs(prev_num) // num * sign
                    ans += prev_num
            elif c in operations:
                if c == "+":
                    sign = 1
                    prev_op = None
                elif c == "-":
                    sign = -1
                    prev_op = None
                elif c == "*":
                    prev_op = "*"
                else:
                    prev_op = "/"  
            i += 1
        # return sum(stk)
        return ans
        