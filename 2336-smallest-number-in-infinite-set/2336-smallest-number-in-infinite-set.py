class SmallestInfiniteSet:

    def __init__(self):
        """
        at most 1000 calls => smallest in [1,1000]
        """
        self.smallest_in_list = [True for _ in range(1000)]

    def popSmallest(self) -> int:
        for i in range(1000):
            if self.smallest_in_list[i]:
                self.smallest_in_list[i] = False
                return i+1
        return None

    def addBack(self, num: int) -> None:
        self.smallest_in_list[num-1] = True

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)