class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        num_removed = 0
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_end:
                num_removed += 1
            else:
                last_end = intervals[i][1]
        return num_removed