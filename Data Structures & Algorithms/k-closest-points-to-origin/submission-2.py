class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distMinHeap = []
        
        for x, y in points:
            dist = math.sqrt((x)**2 + (y)**2)
            heapq.heappush(distMinHeap, (dist, [x, y]))
        
        print(distMinHeap)
        kClosest = []
        for _ in range(k):
            kClosest.append(heapq.heappop(distMinHeap)[1])

        return kClosest