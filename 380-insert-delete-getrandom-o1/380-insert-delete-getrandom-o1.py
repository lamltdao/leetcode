import random

class RandomizedSet:

    def __init__(self):
        """
        set {val: idx}
        [vals]
        """
        self.d = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            prev_idx = self.d[val]
            del self.d[val]
            # move value currently at the end to prev_idx
            self.arr[prev_idx], self.arr[-1] = self.arr[-1], self.arr[prev_idx]
            self.arr.pop()
            if prev_idx < len(self.arr): # handle remove when 1 element
                self.d[self.arr[prev_idx]] = prev_idx
            return True
        return False

    def getRandom(self) -> int:
        random_number = random.randint(0, len(self.arr)-1)
        return self.arr[random_number]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()