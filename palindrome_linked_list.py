'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

'''
import json 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self,head):
        if head.next is None:
            return head
        pointer = head.next
        while pointer is not None:
            temp = pointer.next
            pointer.next = head
            head = pointer
            pointer = temp
        
        return head


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        
        # To find the length of list
        size = 0
        temp = head
        while temp is not None:
            size+=1
            temp = temp.next
        print(size//2)

        # Go its mid-point
        mid_point = head
        for _ in range(size//2):
            mid_point=mid_point.next
        print(mid_point.val)
        
        # reversing half of the linked list
        tail  = Solution().reverse(mid_point)
        print (tail.val)
        print(head.val)
        # print (tail.next.val)

        # Does not work on last point so wrong
        # while head is not tail and head.next is not tail:
        
        for _ in range(size//2):
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True








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

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            
            ret = Solution().isPalindrome(head)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()