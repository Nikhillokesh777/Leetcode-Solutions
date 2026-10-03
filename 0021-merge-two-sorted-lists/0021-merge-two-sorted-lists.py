# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        arr=[]
        while list1:
            arr.append(list1.val)
            list1 = list1.next
        while list2:
            arr.append(list2.val)
            list2 = list2.next
        arr.sort()
        dummy = ListNode(0)
        current  = dummy
        for val in arr:
            current.next = ListNode(val) 
            current = current.next
        return dummy.next




        