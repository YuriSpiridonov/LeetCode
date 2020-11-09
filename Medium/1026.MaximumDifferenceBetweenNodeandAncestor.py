"""
    Given the root of a binary tree, find the maximum value V for which there 
    exist different nodes A and B where V = |A.val - B.val| and A is an 
    ancestor of B.

    A node A is an ancestor of B if either: any child of A is equal to B, 
    or any child of A is an ancestor of B.

    Example:
    Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
    Output: 7
    Explanation: We have various ancestor-node differences, some of which are 
                 given below:
                 |8 - 3| = 5
                 |3 - 7| = 4
                 |8 - 1| = 7
                 |10 - 13| = 3
                 Among all possible differences, the maximum value of 7 is 
                 obtained by |8 - 1| = 7.

    Example:
    Input: root = [1,null,2,null,0,3]
    Output: 3

    Constraints:
        - The number of nodes in the tree is in the range [2, 5000].
        - 0 <= Node.val <= 10^5
"""
#Difficulty: Medium
#27 / 27 test cases passed.
#Runtime: 32 ms
#Memory Usage: 14.7 MB

#Runtime: 32 ms, faster than 94.34% of Python3 online submissions for Maximum Difference Between Node and Ancestor.
#Memory Usage: 14.7 MB, less than 22.68% of Python3 online submissions for Maximum Difference Between Node and Ancestor.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return
        result = 0
        lo_hi = [[root.val, root.val]] # pairs of min and max node values
        queue = [root]
        while queue:
            current = queue.pop(0)
            lo, hi = lo_hi.pop(0)
            result = max(result, abs(lo - hi))
            if current.left:
                queue.append(current.left)
                new_lo = min(lo, current.left.val)
                new_hi = max(hi, current.left.val)
                lo_hi.append([new_lo, new_hi])
            if current.right:
                queue.append(current.right)
                new_lo = min(lo, current.right.val)
                new_hi = max(hi, current.right.val)
                lo_hi.append([new_lo, new_hi])
        return result
