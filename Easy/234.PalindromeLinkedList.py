"""
    Given a singly linked list, determine if it is a palindrome.

    Example:
    Input: 1->2->2->1
    Output: true

    Follow up:
    Could you do it in O(n) time and O(1) space?
"""
#Difficulty: Easy
#26 / 26 test cases passed.
#Runtime: 96 ms
#Memory Usage: 23.8 MB

#Runtime: 96 ms, faster than 31.45% of Python3 online submissions for Palindrome Linked List.
#Memory Usage: 23.8 MB, less than 94.98% of Python3 online submissions for Palindrome Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] != nums[j]:
                return False
            i += 1
            j -= 1
        return True
