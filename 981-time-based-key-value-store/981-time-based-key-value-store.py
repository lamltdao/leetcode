import bisect
class TimeMap:

    def __init__(self):
        """
        {key: [ [timestamp, val] ]}
        """
        self.d = {}
        self.val = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
            self.val[key] = []
        self.d[key].append(timestamp)
        self.val[key].append(value)
    
    def binary_search(self,key, timestamp):
        # return idx i such that self.d[key][:i] <= timestamp, self.d[key][i:] > timestamp
        l = 0
        r = len(self.d[key])-1
        while l <= r:
            m = (l+r) // 2
            if self.d[key][m] > timestamp and (m == 0 or self.d[key][m-1] <= timestamp):
                return m
            elif self.d[key][m] > timestamp:
                r = m-1
            else:
                l = m+1
        return l
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        idx = self.binary_search(key, timestamp)
        if idx >= len(self.d[key]): # timestamp > any prev timestamp
            return self.val[key][-1]
        if idx <= 0: # timestamp < any prev timestamp
            return ""
        return self.val[key][idx-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)