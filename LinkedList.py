"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""
def print_list(head):
    current = head
    while current!=None:
        print current.data
        current=current.next
  """
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 """
def Insert(head, data):
    if head == None:
        head = Node(None)
        head.data = data
    else:
        current = head
        while current.next!=None:
            current = current.next
        current.next = Node()
        current.next.data = data
    return head
    """
  Delete Node at a given position in a linked list
 Node is defined as
  """
  def Delete(head, position):
    if position == 0:
        return head.next
    head.next = Delete(head.next,position-1)
    return head

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 """
 def ReversePrint(head):
    current = head
    prev = None
    next = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
        head = current
    while head is not None:
        print head.data
        head = head.next
      
  
  

 
        
  
  
  
  
  
