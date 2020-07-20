"""
    Given a binary tree, find the leftmost value in the last row of the tree.

    Example:
    Input:
            1
           / \
          2   3
         /   / \
        4   5   6
           /
          7

    Output: 7
    Note: You may assume the tree (i.e., the given root node) is not NULL.
"""
#Difficulty: Medium
#74 / 74 test cases passed.
#Runtime: 40 ms
#Memory Usage: 15.8 MB

#Runtime: 40 ms, faster than 92.04% of Python3 online submissions for Find Bottom Left Tree Value.
#Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Find Bottom Left Tree Value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        left = root.val
        while queue:
            level = []
            length = len(queue)
            while length:
                node = queue.pop(0)
                level.append(node.val)
                length -= 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left = level[0]
        return left
