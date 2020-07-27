"""
    Given a Binary Search Tree and a target number, return true if there exist 
    two elements in the BST such that their sum is equal to the given target.

    Example:
    Input: 
            5
           / \
          3   6
         / \   \
        2   4   7
    
    Target = 9
    Output: True

    Example:
    Input: 
            5
           / \
          3   6
         / \   \
        2   4   7
    
    Target = 28
    Output: False
"""
#Difficulty: Easy
#421 / 421 test cases passed.
#Runtime: 1212 ms
#Memory Usage: 16 MB

#Runtime: 1212 ms, faster than 5.17% of Python3 online submissions for Two Sum IV - Input is a BST.
#Memory Usage: 16 MB, less than 58.51% of Python3 online submissions for Two Sum IV - Input is a BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        result = [False]
        numbers = []
        self.preorder(root, k, result, numbers)
        return max(result)

    def preorder(self, root, k, result, numbers):
        if not root:
            return 0
        if k - root.val in numbers:
            result.append(True)
        numbers.append(root.val)
        self.preorder(root.left, k, result, numbers)
        self.preorder(root.right, k, result, numbers)
