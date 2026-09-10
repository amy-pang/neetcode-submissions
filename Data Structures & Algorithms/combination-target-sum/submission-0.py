class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, runningSum):
            if runningSum == target:
                res.append(subset.copy())
                return
            if i == len(nums) or runningSum > target:
                return
            subset.append(nums[i])
            dfs(i, runningSum + nums[i])

            subset.pop()
            dfs(i + 1, runningSum)
        
        dfs(0, 0)
        return res