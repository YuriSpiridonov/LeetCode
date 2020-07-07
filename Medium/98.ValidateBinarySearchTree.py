"""
    Given a binary tree, determine if it is a valid binary search tree (BST).
    Assume a BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than 
          the node's key.
        - The right subtree of a node contains only nodes with keys greater 
          than the node's key.
        - Both the left and right subtrees must also be binary search trees.

    Example:

            5
           / \
          1   4
             / \
            3   6

    Input: [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
"""
#Difficulty: Medium
#75 / 75 test cases passed.
#Runtime: 44 ms
#Memory Usage: 17 MB

#Runtime: 44 ms, faster than 77.80% of Python3 online submissions for Validate Binary Search Tree.
#Memory Usage: 17 MB, less than 5.06% of Python3 online submissions for Validate Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        order = []
        self.validator(root, order)
        return len(order) == len(set(order)) and order == sorted(order)

    def validator(self, root, order):
        if not root:
            return 0
        self.validator(root.left, order)
        order.append(root.val)
        self.validator(root.right, order)
