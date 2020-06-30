"""
    Given head which is a reference node to a singly-linked list. The value of 
    each node in the linked list is either 0 or 1. The linked list holds the 
    binary representation of a number.
    Return the decimal value of the number in the linked list.
    
    Example:
    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    
    Constraints:
        - The Linked List is not empty.
        - Number of nodes will not exceed 30.
        - Each node's value is either 0 or 1.
"""
#Difficulty: Easy
#102 / 102 test cases passed.
#Runtime: 28 ms
#Memory Usage: 13.7 MB

#Runtime: 28 ms, faster than 79.26% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
#Memory Usage: 13.7 MB, less than 78.12% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def getDecimalValue(self, head: ListNode) -> int:
        binary = 0
        current = head
        while current:
            binary = binary * 10 + current.val
            current = current.next
        return self.binaryToInt(binary)

    def binaryToInt(self, binary):
        number = i = 0
        while binary:
            digit = binary % 10
            number = number + digit * pow(2, i)
            binary //= 10
            i += 1
        return number
