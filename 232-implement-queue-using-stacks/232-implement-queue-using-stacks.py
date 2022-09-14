class MyQueue:

    def __init__(self):
        self.s_main = []
        self.s_sub = []
        self.size = 0
    def push(self, x: int) -> None:
        self.s_main.append(x)
        self.size += 1
    def pop(self) -> int:
        for i in range(self.size-1):
            self.s_sub.append(self.s_main.pop())
        returned_val = self.s_main.pop()
        for i in range(self.size-1):
            self.s_main.append(self.s_sub.pop())
        self.size -= 1
        return returned_val
    def peek(self) -> int:
        for i in range(self.size-1):
            self.s_sub.append(self.s_main.pop())
        returned_val = self.s_main[0]
        for i in range(self.size-1):
            self.s_main.append(self.s_sub.pop())
        return returned_val
    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()