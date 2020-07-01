"""
    Given the root node of a binary search tree (BST) and a value to be inserted 
    into the tree, insert the value into the BST. Return the root node of the 
    BST after the insertion. It is guaranteed that the new value does not exist 
    in the original BST.

    Note that there may exist multiple valid ways for the insertion, as long as 
    the tree remains a BST after insertion. You can return any of them.

    For example, 
    Given the tree:
           
            4
           / \
          2   7
         / \
        1   3

    And the value to insert: 5
    You can return this binary search tree:

             4
           /   \
          2     7
         / \   /
        1   3 5
    
    This tree is also valid:

             5
           /   \
          2     7
         / \   
        1   3
             \
              4

    Constraints:
        - The number of nodes in the given tree will be between 0 and 10^4.
        - Each node will have a unique integer value from 0 to -10^8, inclusive.
        - -10^8 <= val <= 10^8
        - It's guaranteed that val does not exist in the original BST.
"""
#Difficulty: Medium
#35 / 35 test cases passed.
#Runtime: 144 ms
#Memory Usage: 15.9 MB

#Runtime: 144 ms, faster than 64.95% of Python3 online submissions for Insert into a Binary Search Tree.
#Memory Usage: 15.9 MB, less than 73.19% of Python3 online submissions for Insert into a Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        current = root
        while True:
            if not root:
                root = TreeNode(val)
                break
            if current.val > val:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(val)
                    break
            if current.val < val:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(val)
                    break
        return root
