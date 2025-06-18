# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Determine the size of each part
        part_size = length // k
        larger_parts = length % k
        
        # Initialize a list to store the results
        result = []
        
        # Step 3: Split the linked list into parts
        current = head
        for i in range(k):
            sublist_size = part_size + 1 if i < larger_parts else part_size
            if sublist_size == 0:
                result.append(None)
            else:
                sublist_head = current
                for _ in range(sublist_size - 1):
                    current = current.next
                next_node = current.next
                current.next = None
                result.append(sublist_head)
                current = next_node
        
        return result