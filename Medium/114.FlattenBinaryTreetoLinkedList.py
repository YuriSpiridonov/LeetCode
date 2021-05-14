'''
    Given the root of a binary tree, flatten the tree into 
    a "linked list":
        - The "linked list" should use the same TreeNode 
          class where the right child pointer points to the 
          next node in the list and the left child pointer 
          is always null.
        - The "linked list" should be in the same order as 
          a pre-order traversal of the binary tree.

    Example:
    Input: root = [1,2,5,3,4,null,6]
    Output: [1,null,2,null,3,null,4,null,5,null,6]

    Example:
    Input: root = []
    Output: []

    Example:
    Input: root = [0]
    Output: [0]

    Constraints:
        - The number of nodes in the tree is in the range 
          [0, 2000].
        - -100 <= Node.val <= 100
    
    Follow up: Can you flatten the tree in-place (with O(1) 
               extra space)?
'''
#Difficulty: Medium
#225 / 225 test cases passed.
#Runtime: 40 ms
#Memory Usage: 15.2 MB

#Runtime: 40 ms, faster than 45.64% of Python3 online submissions for Flatten Binary Tree to Linked List.
#Memory Usage: 15.2 MB, less than 45.95% of Python3 online submissions for Flatten Binary Tree to Linked List.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        values = []
        self.dfs(root, values)
        for value in values[1:]:
            root.right = TreeNode(value)
            root.left = None
            root = root.right

    def dfs(self, root, values):
        if not root:
            return
        values.append(root.val)
        self.dfs(root.left, values)
        self.dfs(root.right, values)