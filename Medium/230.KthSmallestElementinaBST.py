"""
    Given a binary search tree, write a function kthSmallest to find the kth 
    smallest element in it.

    Example:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
               5
              / \
             3   6
            / \
           2   4
          /
         1
    Output: 3
    Follow up:
    What if the BST is modified (insert/delete operations) often and you need 
    to find the kth smallest frequently? How would you optimize the kthSmallest 
    routine?

    Constraints:
        - The number of elements of the BST is between 1 to 10^4.
        - You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
"""
#Difficulty: Medium
#91 / 91 test cases passed.
#Runtime: 68 ms
#Memory Usage: 17.5 MB

#Runtime: 68 ms, faster than 39.23% of Python3 online submissions for Kth Smallest Element in a BST.
#Memory Usage: 17.5 MB, less than 99.25% of Python3 online submissions for Kth Smallest Element in a BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        visited = []
        self.inorder(root, visited)
        return visited[k-1]

    def inorder(self, root, visited):
        if not root:
            return
        self.inorder(root.left, visited)
        visited.append(root.val)
        self.inorder(root.right, visited)
