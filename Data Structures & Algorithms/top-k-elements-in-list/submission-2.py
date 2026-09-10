class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        unique = {}
        for n in nums:
            unique[n] = unique.get(n, 0) + 1

        for n in unique:
            heapq.heappush(min_heap, (unique[n], n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = [heapq.heappop(min_heap)[1] for i in range(k)]
        
        return res
        
        