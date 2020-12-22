'''
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is 
    defined as:
        - a binary tree in which the left and right subtrees 
          of every node differ in height by no more than 1.

    Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: true

    Example:
    Input: root = [1,2,2,3,3,null,null,4,4]
    Output: false

    Example:
    Input: root = []
    Output: true

    Constraints:
        - The number of nodes in the tree is in the range 
          [0, 5000].
        - -10^4 <= Node.val <= 10^4
'''
#Difficulty: Easy
#228 / 228 test cases passed.
#Runtime: 48 ms
#Memory Usage: 17.9 MB

#Runtime: 48 ms, faster than 80.20% of Python3 online submissions for Balanced Binary Tree.
#Memory Usage: 17.9 MB, less than 75.35% of Python3 online submissions for Balanced Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) >= 0

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
