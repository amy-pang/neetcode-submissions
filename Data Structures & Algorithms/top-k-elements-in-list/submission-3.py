import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} # int, count
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        
        freqToNums = defaultdict(list) # freq, list of nums
        maxFreq = 0
        for n, count in freq.items():
            freqToNums[count].append(n)
            if count > maxFreq:
                maxFreq = count
        
        result = []
        for i in range(maxFreq, 0, -1):
            for n in freqToNums[i]:
                result.append(n)
                if len(result) == k:
                    return result