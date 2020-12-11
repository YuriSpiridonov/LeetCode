'''
    Given a binary tree with the following rules:
        1. root.val == 0
        2. If treeNode.val == x and treeNode.left != null, then 
           treeNode.left.val == 2 * x + 1
        3. If treeNode.val == x and treeNode.right != null, then 
           treeNode.right.val == 2 * x + 2

    Now the binary tree is contaminated, which means all 
    treeNode.val have been changed to -1.

    You need to first recover the binary tree and then implement 
    the FindElements class:
        - FindElements(TreeNode* root) Initializes the object with 
          a contamined binary tree, you need to recover it first.
        - bool find(int target) Return if the target value exists 
          in the recovered binary tree.

    Example:
    Input
    ["FindElements","find","find"]
    [[[-1,null,-1]],[1],[2]]
    Output
    [null,false,true]
    Explanation
                FindElements findElements = 
                                    new FindElements([-1,null,-1]); 
                findElements.find(1); // return False 
                findElements.find(2); // return True 

    Example:
    Input
    ["FindElements","find","find","find"]
    [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
    Output
    [null,true,true,false]
    Explanation
                FindElements findElements = 
                                new FindElements([-1,-1,-1,-1,-1]);
                findElements.find(1); // return True
                findElements.find(3); // return True
                findElements.find(5); // return False

    Example:
    Input
    ["FindElements","find","find","find","find"]
    [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
    Output
    [null,true,false,false,true]
    Explanation
                FindElements findElements = 
                        new FindElements([-1,null,-1,-1,null,-1]);
                findElements.find(2); // return True
                findElements.find(3); // return False
                findElements.find(4); // return False
                findElements.find(5); // return True

    Constraints:
        - TreeNode.val == -1
        - The height of the binary tree is less than or equal 
          to 20
        - The total number of nodes is between [1, 10^4]
        - Total calls of find() is between [1, 10^4]
        - 0 <= target <= 10^6
'''
#Difficulty: Medium
#30 / 30 test cases passed.
#Runtime: 88 ms
#Memory Usage: 20.7 MB

#Runtime: 88 ms, faster than 56.65% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.
#Memory Usage: 20.7 MB, less than 5.65% of Python3 online submissions for Find Elements in a Contaminated Binary Tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.vals = {0}
        self.root = root
        self.recover(self.root)

    def find(self, target: int) -> bool:
        return target in self.vals
    
    def recover(self, root: TreeNode):
        stack = []
        root.val = 0
        curr = root
        while True:
            if curr:
                stack.append(curr)
                if curr.left:
                    curr.left.val = curr.val * 2 + 1
                    self.vals.add(curr.left.val)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if curr.right:
                    curr.right.val = curr.val * 2 + 2
                    self.vals.add(curr.right.val)
                curr = curr.right
            else:
                break


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
