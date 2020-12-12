'''
    Given the root of a binary tree, the depth of each node is 
    the shortest distance to the root.

    Return the smallest subtree such that it contains all the 
    deepest nodes in the original tree.

    A node is called the deepest if it has the largest depth 
    possible among any node in the entire tree.

    The subtree of a node is tree consisting of that node, plus 
    the set of all descendants of that node.

    Note: This question is the same as 1123: 
    https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

    Example:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in 
                 yellow in the diagram.
                 The nodes coloured in blue are the deepest 
                 nodes of the tree.
                 Notice that nodes 5, 3 and 2 contain the 
                 deepest nodes in the tree but node 2 is the 
                 smallest subtree among them, so we return it.

    Example:
    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree.

    Example:
    Input: root = [0,1,3,null,2]
    Output: [2]
    Explanation: The deepest node in the tree is 2, the valid 
                 subtrees are the subtrees of nodes 2, 1 and 
                 0 but the subtree of node 2 is the smallest.

    Constraints:
        - The number of nodes in the tree will be in the 
          range [1, 500].
        - 0 <= Node.val <= 500
        - The values of the nodes in the tree are unique.
'''
#Difficulty: Medium
#58 / 58 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.6 MB

#Runtime: 32 ms, faster than 82.68% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.
#Memory Usage: 14.6 MB, less than 8.28% of Python3 online submissions for Smallest Subtree with all the Deepest Nodes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root, 0)[0]

    def dfs(self, root, depth=0):
        if not root.left and not root.right:
            return root, depth
        if root.left and root.right:
            leftNode, leftDepth = self.dfs(root.left, depth+1)
            rightNode, rightDepth = self.dfs(root.right, depth+1)
            if leftDepth > rightDepth:
                return leftNode, leftDepth
            elif leftDepth < rightDepth:
                return rightNode, rightDepth
            else:
                return root, leftDepth
        if root.left:
            return self.dfs(root.left, depth+1)
        if root.right:
            return self.dfs(root.right, depth+1)
