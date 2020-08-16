"""
    Write a function to delete a node (except the tail) in a singly linked list, 
    given only access to that node.
    Given linked list -- head = [4,5,1,9], which looks like following:

    4->5->1->9

    Example:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list 
                 should become 4 -> 1 -> 9 after calling your function.

    Example:
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list 
                 should become 4 -> 5 -> 9 after calling your function.

    Note:
        - The linked list will have at least two elements.
        - All of the nodes' values will be unique.
        - The given node will not be the tail and it will always be a valid 
          node of the linked list.
        - Do not return anything from your function.
"""
#Difficulty: Easy
#41 / 41 test cases passed.
#Runtime: 40 ms
#Memory Usage: 14.3 MB

#Runtime: 40 ms, faster than 72.82% of Python3 online submissions for Delete Node in a Linked List.
#Memory Usage: 14.3 MB, less than 22.57% of Python3 online submissions for Delete Node in a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node:
            if not node.next.next:
                node.val = node.next.val
                node.next = None
                break
            node.val = node.next.val
            node = node.next
