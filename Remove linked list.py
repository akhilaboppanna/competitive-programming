# definition for singly_linked_list
#class ListNode:
#      def__ init __(self,val=0,next=None):
#           self.val=val
#           self.next=next
class Solution: 
      def removeElements(self,head:Optional[listNode],val:int -> Optional[ListNode]
             prev=ListNode(0)
             temp=prev:
             while head:
                   if head.val!=val:
                      prev.next=head
                      prev=prev.next
             prev.next=None
             return temp.next
    