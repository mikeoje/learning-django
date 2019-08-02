import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, print):
    while node:
        print(str(node.data))

        node = node.next

        if node:
            print(sep)






def mergeLists(head1, head2):
    current1=head1
    current2=head2
    newList=SinglyLinkedList()
    while current1 or current2:
        if not current1:
            newList.insert_node(current2.data)
            current2=current2.next
            continue
        if not current2:
            newList.insert_node(current1.data)
            current1=current1.next
            continue

        if current1.data<current2.data:
            newList.insert_node(current1.data)
            current1=current1.next
        else:
            newList.insert_node(current2.data)
            current2=current2.next
    return newList.head







    
if __name__ == '__main__':
  

    tests = int(input("Enter Number of Test Case "))

    for tests_itr in range(tests):
        llist1_count = int(input("Enter the number of elements in this list "))

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input("Enter the element "))
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input("Enter the number of elements in this list "))

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input("Enter the element "))
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', print)
        print('\n')

  
