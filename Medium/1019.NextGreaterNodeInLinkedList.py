'''
    We are given a linked list with head as the first node.
    Let's number the nodes in the list: node_1, node_2, 
    node_3, ... etc.

    Each node may have a next larger value: for node_i, 
    next_larger(node_i) is the node_j.val such that j > i, 
    node_j.val > node_i.val, and j is the smallest possible 
    choice. If such a j does not exist, the next larger 
    value is 0.

    Return an array of integers answer, where answer[i] = 
    next_larger(node_{i+1}).

    Note that in the example inputs (not outputs) below, 
    arrays such as [2,1,5] represent the serialization of 
    a linked list with a head node value of 2, second node 
    value of 1, and third node value of 5.

    Example:
    Input: [2,1,5]
    Output: [5,5,0]

    Example:
    Input: [2,7,4,3,5]
    Output: [7,0,5,5,0]

    Example:
    Input: [1,7,5,1,9,2,5,1]
    Output: [7,9,9,9,0,5,0,0]

    Note:
        1. 1 <= node.val <= 10^9 for each node in the linked l
           ist.
        2. The given list has length in the range [0, 10000].
'''
#Difficulty: Medium
#76 / 76 test cases passed.
#Runtime: 320 ms
#Memory Usage: 18.6 MB

#Runtime: 320 ms, faster than 66.26% of Python3 online submissions for Next Greater Node In Linked List.
#Memory Usage: 18.6 MB, less than 66.04% of Python3 online submissions for Next Greater Node In Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        result = []
        stack = []
        length = 0
        vals = []

        while head:
            result.append(0)
            length += 1
            vals.append(head.val)
            head = head.next

        for i in range(length):
            if stack:
                while stack and vals[stack[-1]] < vals[i]:
                    result[stack.pop()] = vals[i]
            stack.append(i)
        return result