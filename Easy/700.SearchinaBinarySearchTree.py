"""
    Given the root node of a binary search tree (BST) and a value. You need to 
    find the node in the BST that the node's value equals the given value. 
    Return the subtree rooted with that node. If such node doesn't exist, you 
    should return NULL.

    For example, 
    Given the tree:
            
            4
           / \
          2   7
         / \
        1   3
    
    And the value to search: 2
    You should return this subtree:

          2     
         / \   
        1   3
    
    In the example above, if we want to search the value 5, since there is no 
    node with value 5, we should return NULL.
    Note that an empty tree is represented by NULL, therefore you would see the 
    expected output (serialized tree format) as [], not null.
"""
#Difficulty: Easy
#36 / 36 test cases passed.
#Runtime: 80 ms
#Memory Usage: 15.9 MB

#Runtime: 80 ms, faster than 65.22% of Python3 online submissions for Search in a Binary Search Tree.
#Memory Usage: 15.9 MB, less than 15.46% of Python3 online submissions for Search in a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root or root.val == val:
            return root
        if root.val > val:
            result = self.searchBST(root.left, val)
        else:
            result = self.searchBST(root.right, val)
        return result
