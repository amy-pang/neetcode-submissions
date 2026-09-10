class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start of cycle == duplicate
        fast, slow = 0, 0

        # detecting/getting into cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # slow and fast are inside cycle; need to find start
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow