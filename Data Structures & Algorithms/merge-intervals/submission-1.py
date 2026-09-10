class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        nonoverlapping_intervals = [intervals[0]]
        for start, end in intervals[1:]:
            latest_end = nonoverlapping_intervals[-1][1]
            if start <= latest_end:
                nonoverlapping_intervals[-1][1] = max(latest_end, end)
            else:
                nonoverlapping_intervals.append([start, end])
                
        return nonoverlapping_intervals