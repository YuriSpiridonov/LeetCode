"""
    Given a binary tree, return the sum of values of its deepest leaves.

    Example:

             1
            / \
           2   3
          / \   \
         4   5   6
        /         \
       7           8
    Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
    Output: 15

    Constraints:
        - The number of nodes in the tree is between 1 and 10^4.
        - The value of nodes is between 1 and 100.
"""
#Difficulty: Medium
#15 / 15 test cases passed.
#Runtime: 108 ms
#Memory Usage: 17.4 MB

#Runtime: 108 ms, faster than 53.82% of Python3 online submissions for Deepest Leaves Sum.
#Memory Usage: 17.4 MB, less than 15.88% of Python3 online submissions for Deepest Leaves Sum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = {}
        depth_stick = 0
        self.dfs(root, depth_stick, depth)
        return sum(depth[max(depth, key=int)])

    def dfs(self, root, depth_stick, depth):    
        if not root:
            return
        if not root.left and not root.right:
            if depth_stick not in depth:
                depth[depth_stick] = [root.val]
            else:
                depth[depth_stick].append(root.val)
        depth_stick += 1
        self.dfs(root.left, depth_stick, depth)
        self.dfs(root.right, depth_stick, depth)
