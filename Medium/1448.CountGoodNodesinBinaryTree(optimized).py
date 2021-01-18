'''
    Given a binary tree root, a node X in the tree is named 
    good if in the path from root to X there are no nodes 
    with a value greater than X.

    Return the number of good nodes in the binary tree.

    Example:
             3
            / \
           1   4
          /   / \
         3   1   5
    Input: root = [3,1,4,3,null,1,5]
    Output: 4
    Explanation: - Nodes in blue are good.
                 - Root Node (3) is always a good node.
                 - Node 4 -> (3,4) is the maximum value in 
                   the path starting from the root.
                 - Node 5 -> (3,4,5) is the maximum value 
                   in the path
                 - Node 3 -> (3,1,3) is the maximum value 
                   in the path.

    Example:
             3
            /
           3
          / \
         4   2
    Input: root = [3,3,null,4,2]
    Output: 3
    Explanation: - Node 2 -> (3, 3, 2) is not good, because 
                   "3" is higher than it.

    Example:
    Input: root = [1]
    Output: 1
    Explanation: Root is considered as good.

    Constraints:
        - The number of nodes in the binary tree is in the 
          range [1, 10^5].
        - Each node's value is between [-10^4, 10^4].
'''
#Difficulty: Medium
#63 / 63 test cases passed.
#Runtime: 228 ms
#Memory Usage: 33.5 MB

#Runtime: 228 ms, faster than 92.42% of Python3 online submissions for Count Good Nodes in Binary Tree.
#Memory Usage: 33.5 MB, less than 43.74% of Python3 online submissions for Count Good Nodes in Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, float(-inf))
        return self.count

    def dfs(self, root, max_val):
        if not root:
            return
        if root.val >= max_val:
            self.count += 1
            max_val = root.val
        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)