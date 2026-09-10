class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        for n in nums:
            heapq.heappush(self.max_heap, (-n, n))

    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, (-val, val))
        popped = []
        for _ in range(self.k):
            priority, value = heapq.heappop(self.max_heap)
            popped.append([priority, value])

        kth_value = popped[-1][1]
        for _ in range(self.k):
            priority, value = popped.pop()
            heapq.heappush(self.max_heap, (priority, value))
        return kth_value
        
