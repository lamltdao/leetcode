from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.map = {} # key: [val, freq]
        self.freq_map = {} # freq: OrderedDict() {key: val}
        self.min_freq = 0
        self.capacity = capacity
    def update_freq(self, key):
        prev_freq = self.map[key][1]
        if prev_freq not in self.freq_map:
            self.freq_map[prev_freq] = OrderedDict()
        if key in self.freq_map[prev_freq]:
            del self.freq_map[prev_freq][key]
        self.map[key][1] += 1
        if prev_freq+1 not in self.freq_map:
            self.freq_map[prev_freq+1] = OrderedDict()
        self.freq_map[prev_freq+1][key] = self.map[key]
        # move to front
        self.freq_map[prev_freq+1].move_to_end(key, False)
        # update min_freq
        # condition only holds if prev_freq == min_freq and freq_map[prev_freq] becomes 0 => min now becomes prev_freq +1
        if len(self.freq_map[self.min_freq]) == 0:
            self.min_freq += 1
    def get(self, key: int) -> int:
        if key in self.map:
            self.update_freq(key)
            return self.map[key][0]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key][0] = value
            self.update_freq(key)
        elif len(self.map) < self.capacity:
            self.map[key] = [value, 0]
            self.update_freq(key)
            self.min_freq = 1
        else:
            if len(self.map) > 0:
                # evict lfu
                k,_ = self.freq_map[self.min_freq].popitem()
                del self.map[k]
                if len(self.freq_map[self.min_freq]) == 0:
                    self.min_freq = 1
                # add new key
                self.map[key] = [value,0]
                self.update_freq(key)
                self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)