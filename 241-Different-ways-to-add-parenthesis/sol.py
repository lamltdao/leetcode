operators = set(['+', '-', '*'])
class Solution:
    def executeOp(self, n1, n2, op):
        if op == '+':
            return n1+n2
        elif op == '-':
            return n1-n2
        elif op == '*':
            return n1*n2
    def helper(self, components, start, end):
        if start == end:
            return [components[start]]
        if start + 2 == end:
            op = components[start+1]
            return [self.executeOp(components[start], components[end], op)]
        ans = []
        for i in range(start+1, end):
            if components[i] in operators:
                res_1 = self.helper(components, start, i-1)
                res_2 = self.helper(components, i+1, end)
                for n1 in res_1:
                    for n2 in res_2:
                        ans.append(self.executeOp(n1,n2,components[i]))
        return ans
                
    def diffWaysToCompute(self, expression: str) -> List[int]:
        components = []
        i = 0
        while i < len(expression):
            if expression[i] in operators:
                components.append(expression[i])
                i += 1
            else:
                if i+1 < len(expression) and expression[i+1] not in operators: # 2nd digit of number
                    components.append(int(expression[i:i+2]))
                    i += 2
                else:
                    components.append(int(expression[i]))
                    i += 1
        return self.helper(components, 0, len(components)-1)
