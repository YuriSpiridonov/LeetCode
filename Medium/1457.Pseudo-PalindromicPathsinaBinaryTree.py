'''
    Given a binary tree where node values are digits from 1 
    to 9. A path in the binary tree is said to be 
    pseudo-palindromic if at least one permutation of the 
    node values in the path is a palindrome.

    Return the number of pseudo-palindromic paths going from 
    the root node to leaf nodes.

    Example:
    Input: root = [2,3,1,3,1,null,1]
    Output: 2 
    Explanation: The figure above represents the given binary 
                 ree. There are three paths going from the 
                 root node to leaf nodes: the red path [2,3,3], 
                 the green path [2,1,1], and the path [2,3,1]. 
                 Among these paths only red path and green 
                 path are pseudo-palindromic paths since the 
                 red path [2,3,3] can be rearranged in [3,2,3] 
                 (palindrome) and the green path [2,1,1] can 
                 be rearranged in [1,2,1] (palindrome).

    Example:
    Input: root = [2,1,1,1,3,null,null,null,null,null,1]
    Output: 1 
    Explanation: The figure above represents the given binary 
                 tree. There are three paths going from the 
                 root node to leaf nodes: the green path 
                 [2,1,1], the path [2,1,3,1], and the path 
                 [2,1]. Among these paths only the green path 
                 is pseudo-palindromic since [2,1,1] can be 
                 rearranged in [1,2,1] (palindrome).

    Example:
    Input: root = [9]
    Output: 1

    Constraints:
        - The given binary tree will have between 1 and 
          10^5 nodes.
        - Node values are digits from 1 to 9.
'''
#Difficulty: Medium
#53 / 53 test cases passed.
#Runtime: 540 ms
#Memory Usage: 49.1 MB

#Runtime: 540 ms, faster than 33.16% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.
#Memory Usage: 49.1 MB, less than 96.05% of Python3 online submissions for Pseudo-Palindromic Paths in a Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.result = 0
        self.dfs(root, [])
        return self.result

    def dfs(self, root, path):
        if root:
            path.append(root.val)
            if not root.left and not root.right:
                if self.pathCheck(path):
                    self.result += 1
            if root.left:
                self.dfs(root.left, path)
            if root.right:
                self.dfs(root.right, path)
            path.pop()      

    def pathCheck(self, path):
        count = {}
        odd = 0
        for val in path:
            if val not in count:
                count[val] = 0
            count[val] += 1
        for value in count.values():
            if value % 2:
                odd += 1
            if odd > 1:
                return False
        return True
