# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# leetcode 2
# https://leetcode.com/problems/add-two-numbers/
#   2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dump = ListNode(0) # dummy node
        cur = dump # current node
        carry = 0   
        while l1 or l2: # while l1 or l2 is not None
            if l1: # if l1 is not None
                carry += l1.val 
                l1=l1.next # move to next node
            if l2:
                carry += l2.val
                l2=l2.next
            cur.next = ListNode(carry%10) 
            cur = cur.next
            carry //= 10 # carry = carry // 10 # carry = int(carry / 10)
        if carry == 1:
            cur.next = ListNode(1)
        return dump.next