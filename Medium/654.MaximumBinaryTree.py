'''
    Given an integer array with no duplicates. A maximum tree 
    building on this array is defined as follow:

        1. The root is the maximum number in the array.
        2. The left subtree is the maximum tree constructed f
           rom left part subarray divided by the maximum number.
        3. The right subtree is the maximum tree constructed 
           from right part subarray divided by the maximum 
           number.

    Construct the maximum tree by the given array and output 
    the root node of this tree.

    Example:
    Input: [3,2,1,6,0,5]
    Output: return the tree root node representing the 
            following tree:
           6
        /     \
       3       5
        \     / 
         2   0   
          \
           1

    Note:
        1. The size of the given array will be in the range 
           [1,1000].
'''
#Difficulty: Medium
#107 / 107 test cases passed.
#Runtime: 200 ms
#Memory Usage: 14.9 MB

#Runtime: 200 ms, faster than 72.17% of Python3 online submissions for Maximum Binary Tree.
#Memory Usage: 14.9 MB, less than 31.38% of Python3 online submissions for Maximum Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.dfs(None, nums)

    def dfs(self, root, nums):
        if nums:
            val = max(nums)
            root = TreeNode(val)
            index = nums.index(val)
            root.left = self.dfs(root.left, nums[:index])
            root.right = self.dfs(root.right, nums[index+1:])
        return root
