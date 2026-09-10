from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        val = ""
        l, r = 0, len(self.timemap[key]) - 1
        while l <= r:
            m = (l + r) // 2
            if self.timemap[key][m][0] <= timestamp:
                val = self.timemap[key][m][1]
                l = m + 1
            else:
                r = m - 1
        return val
        
