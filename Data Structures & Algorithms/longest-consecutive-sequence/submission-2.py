class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in nums_set:
                consec = 1
                while n + consec in nums_set:
                    consec += 1
                longest = max(consec, longest)
                
        return longest
            

        