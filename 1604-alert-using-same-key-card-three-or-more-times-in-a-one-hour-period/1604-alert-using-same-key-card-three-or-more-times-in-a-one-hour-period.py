from collections import deque

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def to_minute(time):
            hour = int(time[:2])
            minute = int(time[3:])
            return hour * 60 + minute
        ans = []
        d = {}
        for i in range(len(keyName)):
            name = keyName[i]
            time = to_minute(keyTime[i])
            if name not in d:
                d[name] = []
            # pop for times not in 1-hour interval or in next day
            d[name].append(time)
        for name in d.keys():
            d[name].sort()
        for name in d.keys():
            window_idx = -1
            for i in range(len(d[name])):
                while window_idx+1 < len(d[name]) and d[name][window_idx+1] < d[name][i] - 60:
                    window_idx += 1
                if i - window_idx >= 3:
                    ans.append(name)
                    break
        return sorted(list(ans))