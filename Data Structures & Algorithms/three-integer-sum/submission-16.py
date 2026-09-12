class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nlog(n)
        nums.sort()

        result = []
        # n^2
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if -nums[i] == nums[j] + nums[k]:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1

        return result