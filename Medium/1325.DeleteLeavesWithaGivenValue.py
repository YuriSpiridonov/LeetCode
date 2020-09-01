"""
    Given a binary tree root and an integer target, delete all the leaf nodes 
    with value target.
    Note that once you delete a leaf node with value target, if it's parent 
    node becomes a leaf node and has the value target, it should also be 
    deleted (you need to continue doing that until you can't).

    Example
    Input: root = [1,2,3,2,null,2,4], target = 2
    Output: [1,null,3,null,4]
    Explanation: Leaf nodes in green with value (target = 2) are removed 
                 (Picture in left). 
                 After removing, new nodes become leaf nodes with value 
                 (target = 2) (Picture in center).

    Example:
    Input: root = [1,3,3,3,2], target = 3
    Output: [1,3,null,null,2]

    Example:
    Input: root = [1,2,null,2,null,2], target = 2
    Output: [1]
    Explanation: Leaf nodes in green with value (target = 2) are removed at 
                 each step.

    Example:
    Input: root = [1,1,1], target = 1
    Output: []

    Example:
    Input: root = [1,2,3], target = 1
    Output: [1,2,3]

    Constraints:
        - 1 <= target <= 1000
        - The given binary tree will have between 1 and 3000 nodes.
        - Each node's value is between [1, 1000].
"""
#Difficulty: Medium
#50 / 50 test cases passed.
#Runtime: 72 ms
#Memory Usage: 14 MB

#Runtime: 72 ms, faster than 35.26% of Python3 online submissions for Delete Leaves With a Given Value.
#Memory Usage: 14 MB, less than 90.57% of Python3 online submissions for Delete Leaves With a Given Value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.dfs(root, target)
        if root and root.val == target and not root.left and not root.right:
            root = None
        return root

    def dfs(self, root, target):
        if not root:
            return
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        if root.left and root.left.val == target and not root.left.left and not root.left.right:
            root.left = None
        if root.right and root.right.val == target and not root.right.left and not root.right.right:
            root.right = None
