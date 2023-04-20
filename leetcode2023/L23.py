# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return ListNode().next
        if len (lists)<=1:
            return lists[0]
        temp = ListNode()
        temp.next = lists[0]
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            res = ListNode()
            temp = res
            while list1!=None and list2!=None:
                if list1.val<=list2.val:
                    temp.next=list1
                    list1=list1.next
                else:
                    temp.next=list2
                    list2=list2.next
            if list1!=None:
                temp.next=list1
            if list2!=None:
                temp.next=list2
            return res.next

        for li in lists[1::]:
            temp.next=mergeTwoLists(self,temp.next,li)
        return temp.next 