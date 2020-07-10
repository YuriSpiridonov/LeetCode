"""
    Given a complete binary tree, count the number of nodes.
    Note:
    Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last, is 
    completely filled, and all nodes in the last level are as far left as 
    possible. It can have between 1 and 2h nodes inclusive at the last level h.

    Example:
    Input: 
            1
           / \
          2   3
         / \  /
        4  5 6

    Output: 6
"""
#Difficulty: Medium
#18 / 18 test cases passed.
#Runtime: 100 ms
#Memory Usage: 21.2 MB

#Runtime: 100 ms, faster than 29.09% of Python3 online submissions for Count Complete Tree Nodes.
#Memory Usage: 21.2 MB, less than 77.01% of Python3 online submissions for Count Complete Tree Nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def countNodes(self, root: TreeNode) -> int:
        visited = []
        self.counter(root, visited)
        return len(visited)

    def counter(self, root, visited):
        if not root:
            return
        visited.append(root.val)
        self.counter(root.left, visited)
        self.counter(root.right, visited)
