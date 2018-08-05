
import json
def linked_list_to_number(linked_list):
    multiplier = 1
    value = 0
    # curr = self
    while(linked_list):
        value = value + linked_list.val*multiplier
        linked_list = linked_list.next
        multiplier*=10
    return value
    
def number_to_linked_list(value):
    if value==0:
        return ListNode(0)
    list_node = ListNode(0)
    current = list_node
    while(value!=0):
        current.next=ListNode(value%10)
        # Floor Division, '//' handles even large number
        # Not a good idea to use int(a/10)
        value = value//10
        current = current.next
    return list_node.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = linked_list_to_number(l1)
        # print(val1)
        val2 = linked_list_to_number(l2)
        # print(val2)
        # print(val1+val2)
        return number_to_linked_list(val1+val2)

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
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()