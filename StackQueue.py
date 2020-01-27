class MyQueue:
    def __init__(self, data=None):
        # Initialize this queue, and store data if it exists
        self.length = 0
        # if data is None then initialize queue without head & tail
        if data is None:
            self.head = None
            self.tail = None
        else:
            # if data then initialize queue with head & tail
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        pass

    def enqueue(self, data):
        # Add data to the end of the queue
        self.length += 1
        newNode = Node(data)
        if self.head is None:
            # start and end would be the new node
            self.head = newNode
            self.tail = newNode
        else:
            # new node recorded as next of tail
            self.tail.next = newNode
            # current tail is now the newNode's previous
            newNode.previous = self.tail
            # tail is now recorded as newNode
            self.tail = newNode
        pass

    def dequeue(self):
        # Return the data in the element at the beginning of the queue, or None if the queue is empty
        if self.head is None:
            return None
        else:
            self.length -= 1
            item = self.head.data
            newHead = self.head.next
            # record next as new head
            self.head = newHead
            return item
        pass

    def __len__(self):
        # Return the number of elements in the stack
        return self.length
        pass

class MyStack:
    def __init__(self, data=None):
        # Initialize this stack, and store data if it exists
        self.length = 0
        self.tail = None
        if data == None:
            self.head = None
        else:
            self.head = Node(data)
        pass
    
    def push(self, data):
        # Add data to the beginning of the stack
        self.length += 1
        newNode = Node(data)
        if self.head == None:
            # start and end would be the new node
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            # new node.next recorded as current head
            newNode.next = self.head
            # current tail is now the newNode's previous
            newNode.previous = self.tail
            # head is now recorded as newNode
            self.head = newNode
        
        pass

    def pop(self):
        # Return the data in the element at the beginning of the stack, or None if the stack is empty
        if self.length == 0:
            return None
        item = self.head.data
        # record next as new head
        self.head = self.head.next
        # remove length
        self.length -= 1
        return item
        pass

    def __len__(self):
        # Return the number of elements in the stack
        return self.length
        pass


class Node:
    def __init__(self, data, next=None):
        # Initialize this node, insert data, and set the next node if any
        self.data = data
        self.next = next
        self.previous = None
        pass
