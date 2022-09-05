class MinStack:

    def __init__(self):
        self.stack = []
        self.curMin = None        
    def push(self, val: int) -> None:
        if self.curMin is None:
            self.curMin = val
        else:
            self.curMin = min(self.curMin, val)
        self.stack.append((val, self.curMin))
        
    def pop(self) -> None:
        self.stack.pop()
        self.curMin = self.stack[-1][1] if len(self.stack) > 0 else None
        
    def top(self) -> int:
        return self.stack[-1][0]
    
    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()