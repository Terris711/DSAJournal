from Journal import DSAJournal
from page import page
import pickle
import os


print()

print("Assignment 1 - MINI PROJECT")

print("***Note: To get started reading the journal. You have to go for option 2.a first which creating the Journal first! ")

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
                L.unpickleObj(filename)
                print(L.readCurPage())

            elif activity == 'b':
                    L.move2nextPage()
                    print(L.readCurPage())
            elif activity == 'c':
                    L.move2previousPage()
                    print(L.readCurPage())
            elif activity == 'd':
                    print()
                    print("Publisher: Curtin College")
                    print("Author: Thi Van Anh Duong")
                    print("Discipline: Information Technology")
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
            os.system('clear')
            

    elif int(activity) == 2:

       print("     a. Make a new journal")
       print("     b. Add new page as last page")
       print("     c. Add new page as first page")
       print("     d. Add in after a page number")
       print("     e. Remove first page")
       print("     f. Remove last page")
       print("     g. Edit existing pages")
       print("     h. Store updated journal")
       print("     i. Exit")

       while activity != 'i':   
            if activity == 'a':
                    L = DSAJournal()
                    
                    # Initialize some pages for testing purpose!
                    for i in range(1,26):
                        L.insertLastPage(i,"My journal","Anna","Initial content")

                    # Save Journal to a pickle file
                    filename = input("Enter your file name (with *.pkl): ")
                    L.pickleObj(filename)

                    
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
                    L.removeFirstPage()
                    print()
                    print("You deleted first page!")
                    print()

                    print("Your current journal: ")
                    L.display()
                    print()


            elif activity == 'f':
                    L.removeLastPage()
                    print()
                    print("You deleted last page!")
                    print()

                    print("Your current journal: ")
                    L.display()
                    print()

            elif activity == 'g':
                    position = int(input("Enter page you wanna edit: "))
                    title = input("Enter new title: ")
                    author = input("Enter new author: ")
                    info = input("Enter new information: ")
                    L.editPage(position, title, author, info)

                    print()
                    print("Your new page now: ")
                    print(L.displayPage(position))
                    print()
            elif activity == 'h':
                    L.pickleObj(filename)

            else:
                print("Please enter a valid option!")
            
            print("     a. Make a new journal")
            print("     b. Add new page as last page")
            print("     c. Add new page as first page")
            print("     d. Add in after a page number")
            print("     e. Remove first page")
            print("     f. Remove last page")
            print("     g. Edit existing pages")
            print("     h. Store updated journal")
            print("     i. Exit")
            activity = input("Enter your option: ")
            os.system('clear')

                     
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
    os.system('clear')




