from Journal import DSAJournal
from page import page
import pickle

# Create initial journal
L = DSAJournal()
for i in range(1,10):
    L.insertLastPage(i,"My journal","Anna","Initial content")

print()
# Save Journal to a pickle file
L.pickleObj()
print()

print("Assignment 1 - MINI PROJECT")
print()

print("1. Read journal")
print()

print("2. Start/edit a journal")
print()

print("3. Exit")
print()
activity = input("Enter your option: ")
while int(activity) != 3:
    if int(activity) == 1:
       
       print("     a. Load a journal")
       print("     b. Go to next page")
       print("     c. Go to previous page")
       print("     d. Close the journal")
       print("     e. Exit")

       while activity != 'e':
            if activity == 'a':
                
                # Unpickling file
                print(L.unpickleObj())

            elif activity == 'b':
                    print(L.readCurPage())
            elif activity == 'c':
                    L.move2nextPage()
                    print(L.readCurPage())
            elif activity == 'd':
                    print()
                    print("Publisher: Curtin College")
                    print("Author: Thi Van Anh Duong")
                    print("Published Date: 28 Aug 2022") 
                    print("I hope you have fun <3")
                    print()
                    
            else:
                print("Please enter a valid option!")
            
            print("     a. Load a journal")
            print("     b. Go to next page")
            print("     c. Go to previous page")
            print("     d. Close the journal")
            print("     e. Exit")

            activity = input("Enter your option: ")
            

    elif int(activity) == 2:

       print("     a. Make a new journal")
       print("     b. Add new page as last page")
       print("     c. Add new page as first page")
       print("     d. Add in after a page number")
       print("     e. Edit existing pages")
       print("     f. Store updated journal")
       print("     g. Exit")

       while activity != 'g':   
            if activity == 'a':
                    newJournal = int(input("Enter new Journal name: "))

            elif activity == 'b':
                    newPage = int(input("Enter your page number: "))
                    title = input("Enter your title: ")
                    author = input("Who is the author? ")
                    info = input("Content: ")
                    print()

                    L.insertLastPage(newPage, title, author, info)
                    print("You have added a new page!")
                    print(L.displayPage(newPage))
                    print()

                    print("Your current journal: ")
                    L.display()
                    print()

            elif activity == 'c':
                    newPage = int(input("Enter your page number: "))
                    title = input("Enter your title: ")
                    author = input("Who is the author? ")
                    info = input("Content: ")
                    print()

                    L.insertFirstPage(newPage, title, author, info)
                    print("You have added a new page!")
                    print(L.displayPage(newPage))
                    print()

                    print("Your current journal: ")
                    L.display()
                    print()

            elif activity == 'd':
                    position = int(input("Enter page position you wanna add: "))
                    newPage = int(input("Enter your page number: "))
                    title = input("Enter your title: ")
                    author = input("Who is the author? ")
                    info = input("Content: ")
                    print()

                    L.insertGivenPage(position, newPage, title, author, info)
                    print("You have added a new page!")
                    print(L.displayPage(newPage))
                    print()

                    print("Your current journal: ")
                    L.display()
                    print()

            elif activity == 'e':
                    print('e')
            elif activity == 'f':
                    print('f')
            else:
                print("Please enter a valid option!")
            
            print("     a. Make a new journal")
            print("     b. Add new page as last page")
            print("     c. Add new page as first page")
            print("     d. Add in after a page number")
            print("     e. Edit existing pages")
            print("     f. Store updated journal")
            print("     g. Exit")
            activity = input("Enter your option: ")
            

                     
    else:
        print("Please enter a valid option!")

    print()
    print("1. Read journal")
    print()
    print("2. Start/edit a journal")
    print()
    print("3. Exit")
    print()
    activity = input("Enter your option: ")
    




