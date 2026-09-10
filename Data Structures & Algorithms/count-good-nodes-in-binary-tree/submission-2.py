# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(root, maxVal):
            if not root:
                return 0
            res = 0
            if root.val >= maxVal:
                maxVal = max(maxVal, root.val)
                res += 1
            res += count(root.right, maxVal) + count(root.left, maxVal)
            return res 

        return count(root, root.val)