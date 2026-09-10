class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif threeSum > 0:
                    k -= 1
                else:
                    j += 1
        return res