"""
    Given the root of a binary search tree with distinct values, modify it so 
    that every node has a new value equal to the sum of the values of the 
    original tree that are greater than or equal to node.val.
    As a reminder, a binary search tree is a tree that satisfies these 
    constraints:
        - The left subtree of a node contains only nodes with keys less than 
          the node's key.
        - The right subtree of a node contains only nodes with keys greater 
          than the node's key.
        - Both the left and right subtrees must also be binary search trees.

    Example:
                    4(30)
                   /     \
              1(36)       6(21)
             /     \     /     \
        0(36)     2(35) 5(26)   7(15)
                       \             \
                        3(33)         8(8)

    Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

    Constraints:
        1. The number of nodes in the tree is between 1 and 100.
        2. Each node will have value between 0 and 100.
        3. The given tree is a binary search tree.
    Note: This question is the same as 538: 
          https://leetcode.com/problems/convert-bst-to-greater-tree/
"""
#Difficulty: Medium
#28 / 28 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.8 MB

#Runtime: 28 ms, faster than 89.11% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.
#Memory Usage: 13.8 MB, less than 74.62% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
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
