print('defined Linkelist')
class Node:
    def __init__(self, data):
        self.data= data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None

ll = LinkedList()

#add data
first =Node("20")
second = Node(40)
third = Node(50)


#connecting with next nodes
ll.head =first
first.next = second
second.next= third


print("access Linkelist element: " )

current =ll.head

while current:
    print(current.data, end=" => ")
    current = current.next
  
print(None)


