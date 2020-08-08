"""
    You are given a binary tree in which each node contains an integer value.
    Find the number of paths that sum to a given value.
    The path does not need to start or end at the root or a leaf, but it must 
    go downwards (traveling only from parent nodes to child nodes).
    The tree has no more than 1,000 nodes and the values are in the range 
    -1,000,000 to 1,000,000.

    Example:
    root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
              10
             /  \
            5   -3
           / \    \
          3   2   11
         / \   \
        3  -2   1

    Return 3. The paths that sum to 8 are:
    1.  5 -> 3
    2.  5 -> 2 -> 1
    3. -3 -> 11
"""
#Difficulty: Medium
#126 / 126 test cases passed.
#Runtime: 1012 ms
#Memory Usage: 14.3 MB

#Runtime: 1012 ms, faster than 18.35% of Python3 online submissions for Path Sum III.
#Memory Usage: 14.3 MB, less than 97.53% of Python3 online submissions for Path Sum III.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def pathSum(self, root: TreeNode, summ: int) -> int:
        self.summ = summ
        self.count = 0
        self.dfsFromCurrent(root)
        return self.count

    def dfs(self, root, current_sum):
        if not root:
            return
        if current_sum + root.val == self.summ:
            self.count += 1
        self.dfs(root.left, current_sum + root.val)
        self.dfs(root.right, current_sum + root.val)

    def dfsFromCurrent(self, root):
        if not root:
            return
        self.dfs(root, 0)
        self.dfsFromCurrent(root.left)
        self.dfsFromCurrent(root.right)
