class Solution:
    def calculate(self, s: str) -> int:
        """
        Time: O(s), Space: O(s) bc of stack
        """
        numbers = set([str(i) for i in range(10)])
        operations = set(["+", "-", "*", "/"])
        stk = []
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
                    stk.append(sign * num)
                elif prev_op == "*":
                    stk.append(stk.pop() * num)
                else:
                    n = stk.pop()
                    sign = 1 if n > 0 else -1
                    stk.append(abs(n) // num * sign)
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
        return sum(stk)
        