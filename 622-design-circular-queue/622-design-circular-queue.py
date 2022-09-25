class MyCircularQueue:

    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.queue = [None for _ in range(k)]
        self.size = 0
    def get_next(self, cur_idx):
        if cur_idx+1 < len(self.queue):
            return cur_idx+1
        return 0
    # def get_prev(self, cur_idx):
    #     if cur_idx-1 >= 0:
    #         return cur_idx-1
    #     return len(self.queue)-1
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.rear = self.get_next(self.rear)
            self.queue[self.rear] = value
            self.size += 1
            if self.front == -1: # empty q
                self.front = self.get_next(self.front)
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.front = self.get_next(self.front)
            self.size -= 1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        return self.size <= 0

    def isFull(self) -> bool:
        return self.size >= len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()