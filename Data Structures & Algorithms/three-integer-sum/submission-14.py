class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nlog(n)
        nums.sort()
        # print(nums)
        result = []
        # n^2
        i, j, k = 0, 1, len(nums) - 1
        while i < (len(nums) - 1) and j < k:
            while j < k:
                #print(nums[i], nums[j], nums[k])
                if -nums[i] == nums[j] + nums[k]:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

            i += 1
            while i < (len(nums) - 1) and nums[i] == nums[i - 1]:
                i += 1
            j = i + 1
            k = len(nums) - 1
            

        return result