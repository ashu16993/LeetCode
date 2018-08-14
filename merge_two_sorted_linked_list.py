'''
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(0)
        l3 = ListNode(0)
        start.next = l3
        if(l1==None and l2==None):
            return None
        while(l1!=None and l2!=None):
            l3.next = ListNode(0)
            if(l1.val<l2.val):
                l3.val = l1.val
                l1 =l1.next
            else:
                l3.val = l2.val
                l2 = l2.next
            l3 = l3.next
        
        if(l1!=None):
            l3.val = l1.val
            l3.next = l1.next
        elif(l2!=None):
            l3.val = l2.val
            l3.next = l2.next
        return start.next

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

