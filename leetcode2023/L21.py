# leetcode 21. Merge Two Sorted Lists
# author: ender
# https://leetcode.com/problems/merge-two-sorted-lists/


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                temp.next=ListNode()
                temp.next.val=list1.val
                temp=temp.next
                list1=list1.next
            else:
                temp.next=ListNode()
                temp.next.val=list2.val
                temp=temp.next
                list2=list2.next
        while list1!=None:
            temp.next=ListNode()
            temp.next.val=list1.val
            temp=temp.next
            list1=list1.next
        while list2!=None:
            temp.next=ListNode()
            temp.next.val=list2.val
            temp=temp.next
            list2=list2.next
        return res.next