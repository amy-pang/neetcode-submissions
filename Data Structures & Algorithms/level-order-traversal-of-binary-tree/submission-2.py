# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        # bfs
        while queue:
            qLen = len(queue)
            level = []
            for _ in range(qLen):
                n = queue.popleft()
                if n:
                    level.append(n.val)
                    queue.append(n.left)
                    queue.append(n.right)
            if level:
                res.append(level)
        return res