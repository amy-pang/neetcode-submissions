class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)] # include 0

        for n in nums: # count frequency for each num
            count[n] += 1
        for n, c in count.items(): # invert so idx is freq, value is num
            freq[c].append(n) #list of lists
        
        # find top k frequent nums
        result = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
            
            


