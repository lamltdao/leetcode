class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.arr = []
        for i in range(0, len(encoding), 2):
            freq = encoding[i]
            num = encoding[i+1]
            if freq > 0:
                self.arr.append((freq, num))
        self.cur_idx = 0 # index in self.arr
        self.cur_freq_cnt = 0 # freq counter in self.arr[cur_idx]
    def next(self, n: int) -> int:
        num_exhaust = n
        while self.cur_idx < len(self.arr):
            if self.cur_freq_cnt + num_exhaust <= self.arr[self.cur_idx][0]:
                self.cur_freq_cnt += num_exhaust
                return self.arr[self.cur_idx][1]
            else:
                num_exhaust -= self.arr[self.cur_idx][0] - self.cur_freq_cnt # decrement num_exhaust
                self.cur_freq_cnt = 0 # Reset to 0
                self.cur_idx += 1 # Move to next el in self.arr
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)