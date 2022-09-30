import bisect
class HitCounter:

    def __init__(self):
        self.q = []

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)        

    def getHits(self, timestamp: int) -> int:
        # find idx i such that q[i] <= timestamp and q[i] < q[i+1]
        idx = bisect.bisect_right(self.q, timestamp-300)
        return len(self.q) - idx


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)