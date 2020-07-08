"""
    Invert a binary tree.

    Example:
    Input:
             4
           /   \
          2     7
         / \   / \
        1   3 6   9

    Output:
             4
           /   \
          7     2
         / \   / \
        9   6 3   1

    Trivia:
    This problem was inspired by this original tweet by Max Howell:
        Google: 90% of our engineers use the software you wrote (Homebrew), 
        but you can’t invert a binary tree on a whiteboard so f*** off.
"""
#Difficulty: Easy
#68 / 68 test cases passed.
#Runtime: 40 ms
#Memory Usage: 13.6 MB

#Runtime: 40 ms, faster than 10.02% of Python3 online submissions for Invert Binary Tree.
#Memory Usage: 13.6 MB, less than 94.69% of Python3 online submissions for Invert Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
