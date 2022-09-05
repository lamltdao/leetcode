import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = set(["+", "-", "*", "/"])
        def execute_op(num1, num2, op):
            if op == '+':
                return num1+num2
            elif op == '-':
                return num1-num2
            elif op == '*':
                return num1*num2
            elif op == '/':
                quotient = num1/num2
                return math.ceil(quotient) if quotient < 0 else math.floor(quotient)
        for t in tokens:
            if t in ops:
                num2, num1 = stk.pop(), stk.pop()
                stk.append(execute_op(num1, num2, t))
            else:
                stk.append(int(t))
        return stk[0]