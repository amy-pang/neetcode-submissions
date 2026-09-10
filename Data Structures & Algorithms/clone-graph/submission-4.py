"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        toCopy = collections.deque()
        oldToNew = {}
        toCopy.append(node)
        oldToNew[node] = Node(node.val)
        while toCopy:
            oldNode = toCopy.popleft()
            for oldNeigh in oldNode.neighbors:
                if oldNeigh not in oldToNew:
                    toCopy.append(oldNeigh)
                    oldToNew[oldNeigh] = Node(oldNeigh.val)
                oldToNew[oldNode].neighbors.append(oldToNew[oldNeigh])
        return oldToNew[node]