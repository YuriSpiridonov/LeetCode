'''
    Given the root of a binary tree, return the lowest common 
    ancestor of its deepest leaves.

    Recall that:
        - The node of a binary tree is a leaf if and only if 
          it has no children
        - The depth of the root of the tree is 0. if the depth 
          of a node is d, the depth of each of its children is 
          d + 1.
        - The lowest common ancestor of a set S of nodes, is 
          the node A with the largest depth such that every 
          node in S is in the subtree with root A.

    Note: This question is the same as 865: 
    https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

    Example:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4]
    Output: [2,7,4]
    Explanation: We return the node with value 2, colored in 
                 yellow in the diagram.
                 The nodes coloured in blue are the deepest 
                 leaf-nodes of the tree.
                 Note that nodes 6, 0, and 8 are also leaf 
                 nodes, but the depth of them is 2, but the 
                 depth of nodes 7 and 4 is 3.

    Example:
    Input: root = [1]
    Output: [1]
    Explanation: The root is the deepest node in the tree, 
                 and it's the lca of itself.

    Example:
    Input: root = [0,1,3,null,2]
    Output: [2]
    Explanation: The deepest leaf node in the tree is 2, the 
                 lca of one node is itself.

    Constraints:
        - The number of nodes in the tree will be in the 
          range [1, 1000].
        - 0 <= Node.val <= 1000
        - The values of the nodes in the tree are unique.
'''
#Difficulty: Medium
#81 / 81 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.6 MB

#Runtime: 32 ms, faster than 99.89% of Python3 online submissions for Lowest Common Ancestor of Deepest Leaves.
#Memory Usage: 14.6 MB, less than 27.89% of Python3 online submissions for Lowest Common Ancestor of Deepest Leaves.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
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
