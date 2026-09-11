class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq = 0
        for n in nums:
            m = n
            if n - 1 not in nums_set: 
                while m in nums_set:
                    m += 1
                if m - n > longest_seq:
                    longest_seq = m - n
        
        return longest_seq
