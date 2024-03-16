

# definition for singly_linked_list
#class ListNode:
#      def__ init __(self,val=0,next=None):
#           self.val=val
#           self.next=next
class Solution: 
      def removeElements(self,head:Optional[listNode],val:int -> Optional[ListNode]
             stack=[]
             while head:
                   stack.append(head)
                   head=head.next
              tmp=ListNode()
              dummy=tmp;
              while stack: 
                    tmp.next=stack.pop()
                    tmp=tmp.next
               tmp.next=None
               return dummy.next