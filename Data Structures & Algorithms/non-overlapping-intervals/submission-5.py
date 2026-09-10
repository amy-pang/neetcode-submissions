class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: (pair[1], -pair[0]))
        num_removed = 0
        last_start = float('inf')
        for i, interval in enumerate(intervals[::-1]):
            start, end = interval[0], interval[1]
            print("start, end", start, end)
            if end > last_start:
                num_removed += 1
                last_start = max(start, last_start)
            else:
                last_start = start
            print("last_start, num_removed", last_start, num_removed)
        return num_removed