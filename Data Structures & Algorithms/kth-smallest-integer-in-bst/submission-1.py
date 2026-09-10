# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        res = root.val
        def inOrder(node):
            nonlocal counter, res
            if not node:
                return
            inOrder(node.left)
            counter += 1
            if counter == k:
                res = node.val
                return
            inOrder(node.right)
        inOrder(root)
        return res