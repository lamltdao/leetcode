class Solution:
    def calculate(self, s: str) -> int:
        numbers = set([str(i) for i in range(10)])
        operations = set(["+", "-", "*", "/"])
        """
        4+4*3*2+4
        return 4 + eval
        """
        # Preprocess expression into arr
        arr = []
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
                    arr.append(sign * num)
                elif prev_op == "*":
                    arr.append(arr.pop() * num)
                else:
                    n = arr.pop()
                    sign = 1 if n > 0 else -1
                    arr.append(abs(n) // num * sign)
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
        return sum(arr)
        