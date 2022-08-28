class page:
    
    def __init__(self, title, author, info):
         
        self.title = title
        self.author = author
        self.info = info  
                
    def __str__(self):
        return (" - Title: " + str(self.title) + " - Author: " + str(self.author) + " - Information: " + str(self.info) )
  
        
