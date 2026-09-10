class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        nonoverlapping_intervals = [intervals[0]]
        for start, end in intervals:
            latest_end = nonoverlapping_intervals[-1][1]
            if start <= latest_end:
                nonoverlapping_intervals[-1][1] = max(latest_end, end)
            else:
                nonoverlapping_intervals.append([start, end])
                
        return nonoverlapping_intervals