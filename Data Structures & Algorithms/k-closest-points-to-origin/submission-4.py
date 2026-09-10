class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distMaxHeap = []
        
        for x, y in points:
            dist = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(distMaxHeap, (-dist, [x, y]))
            if len(distMaxHeap) > k:
                heapq.heappop(distMaxHeap)
        res = [point for dist, point in distMaxHeap]
        return res