import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number contacts: ")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory fields")
        print("....................................................................")
        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")

            if j == 1:
                temp.append(int(input("Enter number*: ")))

            if j == 2:
                temp.append(str(input("Enter e-mail address: ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 3:
                temp.append(str(input("Enter date of birth(dd/mm/yy): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

            if j == 4:
                temp.append(str(input("Enter category(Family/Friends/Work/Others): ")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None

        phone_book.append(temp)

    print(phone_book)
    return phone_book

def menu():
    print("********************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("********************************************************************")
    print("\tYou can now perform the following operation on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    choice = int(input("Please enter your choice: "))

    return choice

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter name: ")))
        if i == 1:
            dip.append(str(input("Enter number: ")))
        if i == 2:
            dip.append(str(input("Enter e-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
        if i == 4:
            dip.append(str(input("Enter category(Family/Friends/Work/Others): ")))

    pb.append(dip)
    return pb

def remove_existing(pb):
    query = str(input("Please enter the name of the contact you wish to remove: "))

    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp.

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope

            print(pb.pop(i))
            # The pop function removes entry at index i

            print("This query has now been removed")

            return pb

    if temp == 0:
        # Now if at all any case matches temp should've incremented but if otherwise,
        # temp will remain 0 and that means the query does not exist in this phonebook
        print("Sorry, you have entered an invalid query.\
        Please recheck and try again later.")

        return pb

def delete_all(pb):
    return pb.clear()

def search_existing(pb):
    choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email\n4. DoB\n5. Category(Family/Friends/Work/Others)\
    \nPlease enter: "))

    temp = []
    check = -1

    if choice == 1:
        query = str(input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = int(input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    elif choice == 3:
        query = str(input("Please enter the email of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])

    elif choice == 4:
        query = str(input("Please enter DoB(in dd/mm/yy format ONLY) of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])

    elif choice == 5:
        query = str(input("Please enter the category of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
        # All contacts under query category will be shown using this feature

    else:
        print("Invalid search criteria")
        return -1
    # returning -1 indicates that the search was unsuccessful

    # all the searches are stored in temp and all the results will be displayed with the help of display function

    if check == -1:
        return -1
    # returning -1 indicates that the query did not exist in the directory

    else:
        display_all(temp)
        return check

def display_all(pb):
    if not pb:
    # if display function is called after deleting all contacts then the len will be 0
    # And then without this condition it will throw an error
        print("List is empty: []")

    else:
        for i in range(len(pb)):
            print(pb[i])

def thanks():
    print("********************************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")

# Main function code
print("....................................................................")
print("Hello dear user, welcome to our smartphone directory system")
print("You may now proceed to explore this directory")
print("....................................................................")

ch = 1
pb = initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        d = search_existing(pb)
        if d == -1:
            print("The contact doesn't exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks()
