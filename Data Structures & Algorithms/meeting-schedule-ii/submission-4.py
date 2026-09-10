"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minConcurrent = 0
        meetings = 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        s, e = 0, 0

        while s < len(starts):
            if starts[s] < ends[e]:
                s += 1
                meetings += 1
            else:
                e += 1
                meetings -= 1
            
            minConcurrent = max(meetings, minConcurrent)

        return minConcurrent
                