"""
    Given a Binary Search Tree (BST), convert it to a Greater Tree such that 
    every key of the original BST is changed to the original key plus sum of 
    all keys greater than the original key in BST.

    Example:
    Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13

    Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13

    Note: This question is the same as 1038: 
          https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""
#Difficulty: Easy
#212 / 212 test cases passed.
#Runtime: 88 ms
#Memory Usage: 16.1 MB

#Runtime: 88 ms, faster than 75.61% of Python3 online submissions for Convert BST to Greater Tree.
#Memory Usage: 16.1 MB, less than 60.89% of Python3 online submissions for Convert BST to Greater Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        self.prev = 0
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        root.val = root.val + self.prev
        self.prev = root.val
        self.dfs(root.left)
