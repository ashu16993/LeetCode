'''
Creating your own linkedlist class
'''
class Node:
    def __init__(self):
        self.val = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        curr = self.head
        if(index<0):
            return -1
        if (index==0):
            return self.head.val if self.head.val else -1
        for _ in range(index):
            try:
                curr = curr.next
            except:
                return -1
        return curr.val if curr!=None and curr.val!=None else -1
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head.val==None:
            self.head.val = val
            return
        curr = Node()
        curr.val = val
        curr.next = self.head
        self.head = curr

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        curr = Node()
        curr.next = self.head
        i=0
        if self.head.val == None:
            self.head.val = val
            return True
        while(curr.next!= None):            
            curr = curr.next
        new = Node()
        new.val = val
        curr.next = new
        
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        curr = Node()
        curr.next = self.head
        i=0
        if self.head.val == None and index>0:
            return True
        while(curr!= None):
            if(index==i):
                new = Node()
                new.val = val
                new.next = curr.next
                curr.next = new
                if(i==0):
                    self.head = curr.next
                return True
            else:
                curr = curr.next
                i+=1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        curr = Node()
        curr.next = self.head
        i=0
        while(curr!= None):
            if(index==i):
                try:
                    curr.next = curr.next.next
                    if(i==0):
                        self.head = curr.next
                except:
                    print("Invalid index")
                finally:
                    return True
            else:
                curr = curr.next
                i+=1

 
# # Your MyLinkedList object will be instantiated and called as such:
linkedList = MyLinkedList();

linkedList.addAtHead(7)
linkedList.addAtHead(2)
linkedList.addAtHead(1)
linkedList.addAtIndex(3,0)
linkedList.addAtHead(1)
linkedList.addAtIndex(4,10) # Yahan pe tail galat hogaya
print(linkedList.get(4))
linkedList.deleteAtIndex(2)
linkedList.deleteAtIndex(3)
linkedList.addAtHead(6)
linkedList.addAtTail(4)
print(linkedList.get(3))
linkedList.addAtHead(4)
linkedList.addAtIndex(5,0)
linkedList.addAtHead(6)

# print(linkedList.get(0))
# linkedList.addAtIndex(1,2)
# print(linkedList.get(0))
# print(linkedList.get(1))
# linkedList.addAtIndex(0,1)
# print(linkedList.get(0))
# print(linkedList.get(1))
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  # linked list becomes 1->2->3
# print(linkedList.get(3));            # returns 2
# linkedList.deleteAtIndex(1);  # now the linked list is 1->3
# print(linkedList.get(1));            # returns 3