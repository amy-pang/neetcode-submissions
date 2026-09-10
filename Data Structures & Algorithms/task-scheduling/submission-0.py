class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        todo = {}
        for t in tasks:
            todo[t] = todo.get(t, 0) + 1
        
        tasksMaxHeap = [-val for val in todo.values()]
        heapq.heapify(tasksMaxHeap)
        q = collections.deque()
        
        cycles = 0
        while tasksMaxHeap or q:
            print(cycles, tasksMaxHeap, q)
            if tasksMaxHeap:
                val = heapq.heappop(tasksMaxHeap) + 1 # true val is -val
                if val < 0:
                    q.append([val, cycles + n]) # val, time before it can be added back
            if q and q[0][1] == cycles:
                heapq.heappush(tasksMaxHeap, q.popleft()[0])
            cycles += 1
        return cycles