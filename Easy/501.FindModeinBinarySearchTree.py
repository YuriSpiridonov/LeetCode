"""
    Given a binary search tree (BST) with duplicates, find all the mode(s) 
    (the most frequently occurred element) in the given BST.
    Assume a BST is defined as follows:

        - The left subtree of a node contains only nodes with keys less than or 
          equal to the node's key.
        - The right subtree of a node contains only nodes with keys greater 
          than or equal to the node's key.
        - Both the left and right subtrees must also be binary search trees.

    For example:
    Given BST [1,null,2,2],

           1
            \
             2
            /
           2

    return [2].

    Note: If a tree has more than one mode, you can return them in any order.
    Follow up: Could you do that without using any extra space? (Assume that 
    the implicit stack space incurred due to recursion does not count).
"""
#Difficulty: Easy
#25 / 25 test cases passed.
#Runtime: 64 ms
#Memory Usage: 17.9 MB

#Runtime: 64 ms, faster than 47.70% of Python3 online submissions for Find Mode in Binary Search Tree.
#Memory Usage: 17.9 MB, less than 20.91% of Python3 online submissions for Find Mode in Binary Search Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        result = {}
        self.inorder(root, result)
        max_value = max(result.values())
        return [key for key, value in result.items() if value == max_value]

    def inorder(self, root, result):
        if not root:
            return 0
        self.inorder(root.left, result)
        if root.val in result:
            result[root.val] += 1
        else:
            result[root.val] = 1
        self.inorder(root.right, result)
