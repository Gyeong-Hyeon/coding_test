"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        visited, to_visit = {1: Node(val=node.val)}, [node]
        
        while to_visit:
            me = to_visit.pop()
            if not visited.get(me.val):
                new_me = Node(val=me.val)
                visited[me.val] = new_me
            else:
                new_me = visited[me.val]
                if new_me.neighbors:
                    continue

            new_neighbors = []
            for neighbor in me.neighbors:
                if not visited.get(neighbor.val):
                    new_neighbor = Node(val=neighbor.val)
                    visited[neighbor.val] = new_neighbor
                    to_visit.append(neighbor)
                else:
                    new_neighbor = visited[neighbor.val]
                new_neighbors.append(new_neighbor)
            new_me.neighbors = new_neighbors
        return visited[1]