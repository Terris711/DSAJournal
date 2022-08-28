from page import page

class DSANode():        

    def __init__(self, pageNum = None, title = None, author = None, info = None, content = object, pointer = None, previous = None):
        
        self.pageNum = pageNum # act like key
        self.content = page(title, author, info)
        self.pointer = pointer # point to the next node
        self.previous = previous # point to the previous node

    def __str__(self):
        return ("Page Number: " + str(self.pageNum) + " Content: " + str(self.content))

