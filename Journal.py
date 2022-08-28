from page import page
from DSAListNode import DSANode
import pickle


class DSAJournal():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.curPage = None

        
    def __str__(self):
        
        result = ""

        curPage = self.head
        while curPage is not None:
            result += str(curPage.content) + "-->"
            curPage = curPage.pointer
        
        print()
        return result


    def getCount(self):
        return self.count


    def display(self):
        curPage = self.head
        while curPage is not None:
            print(curPage.content, end = "-->")
            curPage = curPage.pointer
        print()

    def displayPage(self, pageId):
        curPage = self.head
        while curPage is not None:
                if curPage.pageNum == pageId:
                    return curPage
                curPage = curPage.pointer
        print()

         

    def __iter__(self):
        curPage = self.head
        while curPage is not None:
            yield curPage.pageNum
            curPage = curPage.pointer
        
    def isEmpty(self):
        return self.head == None

    def getSize(self):
        count = 0
        curPage = self.head
        while curPage is not None:
            count += 1
            curPage = curPage.pointer
        print(count)

    def insertFirstPage(self, pageNum, title, author, info):
        if self.isEmpty():
            self.head = DSANode(pageNum, title, author, info)

        else:
            newPage = DSANode(pageNum, title, author, info)
            newPage.pointer = self.head
            if self.head is not None:
                self.head.previous = newPage
            self.head = newPage
            self.count += 1
            
            

    def insertLastPage(self, pageNum, title, author, info):
        newPage = DSANode(pageNum, title, author, info)
        newPage.pointer = None

        if self.head is None:
            newPage.previous = None
            self.head = newPage
        else: 
            lastPage = self.head
            while lastPage.pointer is not None:
                lastPage = lastPage.pointer
            lastPage.pointer = newPage
            newPage.previous = lastPage
        self.count += 1
         
    
    def insertGivenPage(self, prePage, newData, title, author, info):
        prePage = self.head
        # Base case
        if prePage is None:
                print("This page does not exist!")
                return
        
        # Create a new page + put in data
        newPage = DSANode(newData, title, author, info)

        # Make the next of new page as next of prePage
        newPage.pointer = prePage.pointer
        # Make next of prePage as newPage
        prePage.pointer = newPage
        #newPage.previous = prePage

    # Change previous of newPage's next page
        if newPage.pointer is not None:
                newPage.pointer.previous = newPage

        self.count += 1


    def peekFirst(self):
        return self.head.pageNum

    def peekLast(self, Page):
        Page = Page.head
        while Page.pointer is not None:
            Page = Page.pointer
        return Page.pageNum

    def removeFirstPage(self):
        if self.isEmpty():
            print("Journal is empty!")
        else:
            delPage = self.head.pageNum
            self.head = self.head.pointer
            self.count -= 1
        return delPage

    def removeLastPage(self):
        if self.isEmpty():
            print("Journal is empty!")
        else:
            curPage = self.head
            # Find  the last node            
            while curPage.pointer is not None: 
                curPage = curPage.pointer
            
            if curPage == self.head:
            #when only one node left, remove head
                self.head = None
            else:                       
                curPage.previous.pointer= None
            
            self.count -= 1
    
    def readCurPage(self):
        if self.curPage is None:
            self.curPage = self.head

        return self.curPage.__str__()       

    def move2previousPage (self):
        if self.isEmpty():
                print("Already at first page. Cannot move further!")
        else:
                curPage = self.pageNum
                return curPage.previous    
    
    def move2nextPage (self):
        if self.isEmpty():
                print("Already at last page. Cannot move further!")
        else:
                print(self.curPage.__str__())
                #curPage = self.curPage.previous
                return curPage


    def pickleObj(self):
        
        print("Saving Journal to file ....")
        
        try:
            with open("myJournal.pkl", "wb") as f:
                pickle.dump(self, f)
            f.close()
        except IOError:
            print("Something went wrong!!!")



    
    def unpickleObj(self):
        try:
            with open("myJournal.pkl", "rb") as f:
                Journal = pickle.load(f)
            f.close()
        except IOError:
            print("File does not exist!!!")

        return Journal

    
           
