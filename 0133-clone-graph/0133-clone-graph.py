"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new_nodes_map = {}

        def cloneNode(current_node):
            if current_node == None:
                return None
                
            if current_node.val in new_nodes_map:
                return new_nodes_map[current_node.val]

            new_node = Node()
            new_node.val = current_node.val
            new_nodes_map[new_node.val] = new_node

            for neighbor in current_node.neighbors:
                new_node.neighbors.append(cloneNode(neighbor))
            return new_node
        return cloneNode(node)

        