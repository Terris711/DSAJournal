from Journal import DSAJournal
from page import page
from DSAListNode import DSANode

L = DSAJournal()
for i in range(5):
    L.insertLastPage(i,"My journal","Anna","Initial content")
    
print()
print("Your current list: ")
L.display()
print()

print("Now, we will try to modify the list!")
print()

print("1. Insert from the head")
print("2. Insert from the tail")
print("3. Delete from the head")
print("4. Delete from the tail")
print("5. Size of list")
print("6. Testing ITERATION")
print("7. Exit")
print("8. Insert at given page")
print()
activity = int(input("Enter your option: "))
while activity != 7:
    if activity == 1:
        L.insertFirstPage(10,"Women", "Anna", "Women like banana")
        L.display()
    elif activity == 2:
        newKey = int(input("Enter new value: "))
        L.insertLastPage(9, "Men","Nasal","Men like women")
        L.display()
    elif activity == 3:
        L.removeFirstPage()
        L.display()
    elif activity == 4:
        L.removeLastPage()
        L.display()
    elif activity == 5:
        L.getSize();
    elif activity == 8:
        L.insertGivenPage(L.head.pointer.pointer,6, "Banana", "James Mc", "It is difficult to delivery");
        L.display()
    elif activity == 6:
        iteration = iter(L)
        data = next(iteration)
        for data in L:
            print(data, end = "-->")
        print()
    elif activity == 9:
        print(L.displayPage(10))
    else:
        print("Please enter a valid option!")
    activity = int(input("Enter your option: "))






