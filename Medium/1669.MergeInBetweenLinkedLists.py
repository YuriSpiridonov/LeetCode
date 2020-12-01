"""
    You are given two linked lists: list1 and list2 of sizes n and m 
    respectively.

    Remove list1's nodes from the ath node to the bth node, and put list2 
    in their place.

    The blue edges and nodes in the following figure incidate the result:

    Build the result list and return its head.

    Example:
    Input: list1 = [0,1,2,3,4,5], 
           a = 3, 
           b = 4, 
           list2 = [1000000,1000001,1000002]
    Output: [0,1,2,1000000,1000001,1000002,5]
    Explanation: We remove the nodes 3 and 4 and put the entire list2 in 
                 their place. The blue edges and nodes in the above figure 
                 indicate the result.

    Example:
    Input: list1 = [0,1,2,3,4,5,6], 
           a = 2, 
           b = 5, 
           list2 = [1000000,1000001,1000002,1000003,1000004]
    Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
    Explanation: The blue edges and nodes in the above figure indicate 
                 the result.

    Constraints:
        - 3 <= list1.length <= 10^4
        - 1 <= a <= b < list1.length - 1
        - 1 <= list2.length <= 10^4
"""
#Difficulty: Medium
#60 / 60 test cases passed.
#Runtime: 452 ms
#Memory Usage: 19.9 MB

#Runtime: 452 ms, faster than 65.67% of Python3 online submissions for Merge In Between Linked Lists.
#Memory Usage: 19.9 MB, less than 99.25% of Python3 online submissions for Merge In Between Linked Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        curr = list1.next
        while curr.val != a:
            prev = curr
            curr = curr.next
        prev.next = list2
        while curr.val != b:
            curr = curr.next
        while prev.next:
            prev = prev.next
        prev.next = curr.next
        return list1
