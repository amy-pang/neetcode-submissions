class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, (-s, s))
        
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)[1]
            y = heapq.heappop(max_heap)[1]
            if x > y:
                x = x -y
                heapq.heappush(max_heap, (-x, x))

        return max_heap[0][1] if len(max_heap) > 0 else 0