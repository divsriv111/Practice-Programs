class Node:
    def __init__(self, data=None, next=None) -> None:
        self.Data = data
        self.Next = next

    def setData(self, data):
        self.Data = data

    def setNext(self, next):
        self.Next = next

    def getData(self):
        return self.Data

    def getNext(self):
        return self.Next

    def hasNext(self):
        return self.Next != None


class LinkedList:
    def __init__(self, node=None) -> None:
        self.Head = node

    def display(self):
        curr = self.Head
        count = 0
        while curr != None:
            print(f"{curr.Data} -> ", end=" ")
            count += 1
            curr = curr.Next
        return count
