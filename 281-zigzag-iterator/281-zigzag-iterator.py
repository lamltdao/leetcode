class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.idx1 = -1
        self.idx2 = -1
        self.v1 = v1
        self.v2 = v2
        self.is_v1_turn = True

    def next(self) -> int:
        ans = None
        if self.is_v1_turn:
            if self.idx1 + 1 < len(self.v1):
                self.idx1 += 1
                ans = self.v1[self.idx1]
            else:
                self.idx2 += 1
                ans = self.v2[self.idx2]
        else:
            if self.idx2 + 1 < len(self.v2):
                self.idx2 += 1
                ans = self.v2[self.idx2]
            else:
                self.idx1 += 1
                ans = self.v1[self.idx1]
        self.is_v1_turn = not self.is_v1_turn
        return ans

    def hasNext(self) -> bool:
        return self.idx1+1 < len(self.v1) or self.idx2+1 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())