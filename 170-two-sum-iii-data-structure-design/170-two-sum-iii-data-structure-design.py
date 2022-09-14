class TwoSum:

    def __init__(self):
        self.d = {}        

    def add(self, number: int) -> None:
        if number not in self.d:
            self.d[number] = 0
        self.d[number] += 1

    def find(self, value: int) -> bool:
        for k in self.d.keys():
            if value-k in self.d and (value-k != k or self.d[k] >= 2):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)