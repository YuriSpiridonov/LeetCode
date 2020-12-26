'''
    Given a binary tree, return the sum of values of nodes 
    with even-valued grandparent.  (A grandparent of a node 
    is the parent of its parent, if it exists.)

    If there are no nodes with an even-valued grandparent, 
    return 0.

    Example:
    Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
    Output: 18
    Explanation: The red nodes are the nodes with even-value 
                 grandparent while the blue nodes are the 
                 even-value grandparents.

    Constraints:
        - The number of nodes in the tree is between 1 and 
          10^4.
        - The value of nodes is between 1 and 100.
'''
#Difficulty: Medium
#14 / 14 test cases passed.
#Runtime: 256 ms
#Memory Usage: 17.8 MB

#Runtime: 256 ms, faster than 5.15% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
#Memory Usage: 17.8 MB, less than 26.67% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return 0
        if not root.val % 2:
            self.two_step_dfs(root.left)
            self.two_step_dfs(root.right)
        self.dfs(root.left)
        self.dfs(root.right)

    def two_step_dfs(self, root, step=0):
        if not root:
            return 0
        if step == 1:
            self.result += root.val
        self.two_step_dfs(root.left, step+1)
        self.two_step_dfs(root.right, step+1)
