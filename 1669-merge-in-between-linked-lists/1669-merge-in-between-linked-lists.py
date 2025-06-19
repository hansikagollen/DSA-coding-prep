# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev=list1
        temp1=list1
        curr=list1
        a-=1

        while temp1 and a>0:
            temp1=temp1.next
            prev=temp1
            curr=list1
            a-=1

        temp1=list1

        while temp1 and b>0:
            temp1=temp1.next
            curr=temp1
            b-=1

        temp2=list2

        while temp2.next:
            temp2=temp2.next

        prev.next=list2
        temp2.next=curr.next

        return list1        