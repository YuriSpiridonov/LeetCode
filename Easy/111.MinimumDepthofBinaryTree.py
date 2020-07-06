"""
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the 
    root node down to the nearest leaf node.

    Note: A leaf is a node with no children.

    Example:
    Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
    return its minimum depth = 2.
"""
#Difficulty: Easy
#41 / 41 test cases passed.
#Runtime: 36 ms
#Memory Usage: 15.8 MB

#Runtime: 36 ms, faster than 96.45% of Python3 online submissions for Minimum Depth of Binary Tree.
#Memory Usage: 15.8 MB, less than 19.03% of Python3 online submissions for Minimum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right and left < right or right == 0:
            return left + 1
        else:
            return right + 1
