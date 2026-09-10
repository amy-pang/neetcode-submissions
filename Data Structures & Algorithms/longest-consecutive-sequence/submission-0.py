class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums)
        longest = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                longest[i] = longest[i - 1] + 1
        
        largest = 0
        for n in longest:
            if n > largest:
                largest = n

        return largest