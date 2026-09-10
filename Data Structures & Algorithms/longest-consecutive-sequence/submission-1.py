class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if n-1 in nums_set:
                continue
            consec = 1
            m = n + 1
            while m in nums_set:
                consec += 1
                m += 1
            longest = max(consec, longest)
                
        return longest
            

        