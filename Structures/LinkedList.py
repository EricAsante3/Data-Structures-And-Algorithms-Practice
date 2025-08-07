class Node:
    def __init__(self, value):
        self.value = value

        self.prev = None
        
        self.next = None



class LinkedList:
    def __init__(self, value):
        self.head = self.tail = Node(value)


    def AddToStart(self, value):
        newHead = Node(value)
        newHead.next = self.tail
        self.tail.prev = newHead
        self.head = newHead


    def AddToEnd(self, value):
        newTail = Node(value)
        newTail.prev = self.tail
        self.tail.next = newTail
        self.tail = newTail


    def PrintFromHead(self):

        currnode = self.head
        while currnode.next != None:
            print(currnode.value)
            currnode = currnode.next

        print(currnode.value)


    def PrintFromTail(self):

        currnode = self.tail
        while currnode.prev != None:
            print(currnode.value)
            currnode = currnode.prev
        print(currnode.value)




newlist = LinkedList(9)


newlist.AddToStart(18)

newlist.PrintFromHead()
newlist.PrintFromTail()



newlist.AddToEnd(69)
newlist.PrintFromHead()
