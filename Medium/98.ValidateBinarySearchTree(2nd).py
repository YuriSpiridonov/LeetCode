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
#Runtime: 60 ms
#Memory Usage: 16.1 MB
    
#Runtime: 60 ms, faster than 23.93% of Python3 online submissions for Validate Binary Search Tree.
#Memory Usage: 16.1 MB, less than 74.97% of Python3 online submissions for Validate Binary Search Tree. 
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        order = []
        self.validator(root, order)
        for i in range(1, len(order)):
            if order[i-1] >= order[i]:
                return False
        return True

    def validator(self, root, order):
        if not root:
            return 0
        self.validator(root.left, order)
        order.append(root.val)
        self.validator(root.right, order) 
