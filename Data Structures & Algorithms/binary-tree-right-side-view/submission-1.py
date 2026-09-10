# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.max_level = 0

        def traverse(root, level):
            if not root:
                return
            
            if level > self.max_level:
                self.res.append(root.val)
                self.max_level = level
            traverse(root.right, level + 1)
            traverse(root.left, level + 1)
        
        traverse(root, 1)
        return self.res