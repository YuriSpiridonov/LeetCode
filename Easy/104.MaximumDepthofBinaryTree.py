"""
    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the 
    root node down to the farthest leaf node.

    Note: A leaf is a node with no children.

    Example:
    Given binary tree [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
    return its depth = 3.
"""
#Difficulty: Easy
#39 / 39 test cases passed.
#Runtime: 28 ms
#Memory Usage: 15.3 MB

#Runtime: 28 ms, faster than 99.81% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 15.3 MB, less than 68.94% of Python3 online submissions for Maximum Depth of Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return left + 1 if left > right else right + 1
