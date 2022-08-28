from DSAListNode import DSANode
from DSADoubledlist import DSADoubledList

class DSAQueue(DSADoubledList):
    def __init__(self):
        super().__init__()        

    def isEmpty(self):
        super().isEmpty()

    def enqueue(self, item):  #Adding more item to the list
        super().insertLast(item)

    def dequeue(self):
        return super().removeFirst()


