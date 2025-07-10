"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        node_map = {}
        temp = head

        while temp :
            new_node = ListNode(temp.val)
            node_map[temp] = new_node
            temp = temp.next
            
        temp = head
        
        while temp :
            curr = node_map[temp]

            if temp.next:
                curr.next = node_map[temp.next]
            else:
                curr.next = None

            if temp.random:
                curr.random = node_map[temp.random]
            else:
                curr.random = None

            temp = temp.next
        
        return node_map[head]
        
