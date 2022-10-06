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
        
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        idx = bisect.bisect_right(self.d[key], timestamp)
        if idx >= len(self.d[key]): # timestamp > any prev timestamp
            return self.val[key][-1]
        if idx <= 0: # timestamp < any prev timestamp
            return ""
        return self.val[key][idx-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)