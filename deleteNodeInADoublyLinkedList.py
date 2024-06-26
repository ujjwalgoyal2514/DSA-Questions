"""Given a doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1) in a doubly linked list and return the head of the doubly Linked list.

Examples:

Input: LinkedList = 1 <--> 3 <--> 4, x = 3
Output: 1 3  
Explanation: 
After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.
 
Input: LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
Output: 5 2 9
Explanation:

Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
2 <= size of the linked list(n) <= 105
1 <= x <= n
1 <= node.data <= 109

"""
class Solution:
    def delete_node(self, head, x):
        #code here
        
        cur = head
        prev=None
        temp=None
        count=1
        while count!=x:
            prev=cur
            cur=cur.next
            count+=1
        
        
        if prev is not None:
            prev.next=cur.next
        else:
            cur=cur.next #if x is 1
            cur.prev=None
            return cur
        if cur.next is not None: # if x is not last
            cur.next.prev=prev
        
        return head