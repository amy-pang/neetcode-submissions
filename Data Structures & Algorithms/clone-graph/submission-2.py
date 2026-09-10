"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyHead = None
        
        if node:
            toCopy = collections.deque()
            visited = {}
            copyHead = Node(node.val)
            toCopy.append((copyHead, node))
            visited[node.val] = copyHead
            while toCopy:
                copyNode, oldNode = toCopy.popleft()
                print("node val", copyNode.val, oldNode.val)
                for oldNeigh in oldNode.neighbors:
                    if oldNeigh.val not in visited:
                        newNeigh = Node(oldNeigh.val)
                        toCopy.append((newNeigh, oldNeigh))
                        visited[oldNeigh.val] = newNeigh
                    else:
                       newNeigh = visited[oldNeigh.val]
                    copyNode.neighbors.append(newNeigh)
                for n in copyNode.neighbors:
                    print("neighbors", n.val)
        return copyHead