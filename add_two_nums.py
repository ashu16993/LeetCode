# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# from copy import deepcopy,copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    list_node = ListNode(0)
    current = list_node

    ''' Failed ways.. '''
    # list_node = list_node_temp = None
    # ListNode(value%10)
    # value = int(value/10)
    # list_node_temp = deepcopy(list_node)
    # list_node.next = list_node_temp
    # value = int(value/10)
    while(value!=0):
        current.next=ListNode(value%10)
        value = int(value/10)
        current = current.next


        '''3rd Failed way'''
        # temp = ListNode(value%10)
        # if list_node is None:
        #     list_node = temp
        # else:
        #     list_node_temp = copy(list_node)
        #     while(list_node_temp):
        #         list_node_temp = list_node_temp.next
        #     list_node_temp = temp
        # value = int(value/10)

        '''2nd Failed Way'''
        # if list_node is not None:
        #     list_node_temp = temp
        # else:
        #     list_node = temp
        #     list_node_temp = temp
        # value = int(value/10)

        '''1st failed way'''
        # list_node_temp.next = ListNode(value%10)
        # if list_node.next is None:
        #     list_node.next= list_node_temp.next
        # # list_node_temp.next = list_node_temp
        # value = int(value/10)
    return list_node.next


class Solution:
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = linked_list_to_number(l1)
        print(val1)
        val2 = linked_list_to_number(l2)
        print(val2+val1)
        return number_to_linked_list(val1+val2)




if __name__=="__main__":
    # list_node1 = ListNode(2)
    # list_node2 = ListNode(4)
    # list_node3 = ListNode(3)
    # list_node1.next = list_node2
    # list_node2.next = list_node3

    # list_node4 = ListNode(4)
    # list_node5 = ListNode(3)
    # list_node4.next = list_node5
    list_node1 = number_to_linked_list(3425)
    list_node2 = number_to_linked_list(23476)
    test = Solution()
    test.addTwoNumbers(list_node1,list_node2)
    