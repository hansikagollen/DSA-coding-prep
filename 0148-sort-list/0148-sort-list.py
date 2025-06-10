# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        arr=[]
        dummy=head
        while dummy is not None:
            arr.append(dummy.val)
            dummy=dummy.next
        arr.sort()

        new_head=ListNode(arr[0])
        temp=new_head
        for i in range(1,len(arr)):
            temp.next=ListNode(arr[i])
            temp=temp.next
        return new_head
        