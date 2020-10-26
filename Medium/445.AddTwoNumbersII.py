"""
    You are given two non-empty linked lists representing two non-negative 
    integers. The most significant digit comes first and each of their nodes 
    contain a single digit. Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the 
    number 0 itself.

    Follow up:
    What if you cannot modify the input lists? In other words, reversing the 
    lists is not allowed.

    Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
"""
#Difficulty: Medium
#1563 / 1563 test cases passed.
#Runtime: 72 ms
#Memory Usage: 14.1 MB

#Runtime: 72 ms, faster than 76.66% of Python3 online submissions for Add Two Numbers II.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Add Two Numbers II.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number = 0
        stack = []
        number += self.LinkedListToInteger(l1)
        number += self.LinkedListToInteger(l2)
        if number == 0:
            stack.append(0)
        while number:
            stack.append(number % 10)
            number //= 10
        l3 = ListNode(stack.pop())
        node = l3
        while stack:
            node.next = ListNode(stack.pop())
            node = node.next
        return l3
    
    def LinkedListToInteger(self, ll):
        n = 0
        while ll:
            n = n * 10 + ll.val
            ll = ll.next
        return n
