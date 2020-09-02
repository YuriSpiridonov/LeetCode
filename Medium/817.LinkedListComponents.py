"""
    We are given head, the head node of a linked list containing unique integer 
    values.
    We are also given the list G, a subset of the values in the linked list.
    Return the number of connected components in G, where two values are 
    connected if they appear consecutively in the linked list.

    Example:
    Input: 
    head: 0->1->2->3
    G = [0, 1, 3]
    Output: 2
    Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected 
                 components.

    Example:
    Input: 
    head: 0->1->2->3->4
    G = [0, 3, 1, 4]
    Output: 2
    Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and 
                 [3, 4] are the two connected components.

    Note:
        - If N is the length of the linked list given by head, 1 <= N <= 10000.
        - The value of each node in the linked list will be in the range 
          [0, N - 1].
        - 1 <= G.length <= 10000.
        - G is a subset of all values in the linked list.
"""
#Difficulty: Medium
#57 / 57 test cases passed.
#Runtime: 3932 ms
#Memory Usage: 17.9 MB

#Runtime: 3932 ms, faster than 11.92% of Python3 online submissions for Linked List Components.
#Memory Usage: 17.9 MB, less than 78.42% of Python3 online submissions for Linked List Components.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        count = 0
        prev = None
        while head:
            if head.val in G and not prev in G:
                count += 1
            prev = head.val
            head = head.next
        return count
