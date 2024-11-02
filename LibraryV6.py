import time  
from datetime import datetime  
import sys 
admins = {'superadmin': 'superadmin', 'admin': 'admin','admin2': 'admin2', } 
library_pass = '1234'

#Common Functions 

#1. Function to add files
def add_to_file(file_name, content, quantity, email, phone_number):
    if quantity == None: 
        if (
            not content.strip() or not email.strip() or not phone_number.strip()
        ):  
            print(
                "INVALID INPUT ❎\nInformation has to be provided"
            )  
            return
        with open(file_name, "a") as f: 
            timestamp = time.strftime(
                "%d-%m-%Y %I:%M:%p"
            )  
            f.write(
                f"{content}| {email}| {phone_number} Added on {timestamp}\n"
            )  
            print(f"{content} added to {file_name}")  
    else:  
        if not content.strip() or not quantity.strip(): 
            print("INVALID INPUT ❎\nInformation has to be provided")
            return
        try:
            quantity = int(quantity)
        except ValueError:
            print("INVALID INPUT ❎\nQuantity must be an integer")
            return
        with open(file_name, "a") as f: 
            timestamp = time.strftime("%d-%m-%Y %I:%M:%p")
            f.write(f"{content}| amount available {quantity}| Added on {timestamp}\n")
            print(f"{content} added to {file_name}")
            
#2. Function to view files
def view_from_file(file_name):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"{file_name} not found")
    
#3. Fucntion to search things in file
def search_in_file(file_name, search_term):
  
    if not search_term.strip():
        print("Invalid input ❎\nSEARCH TERM cannot be blank.")
        return None
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            found = False  
            for line in lines:
                strippedLine = line.strip()  #
                if strippedLine and search_term.lower() in strippedLine.lower():  
                    print(f"Found: {strippedLine}")
                    found = True  
                    return strippedLine
            if not found:  
                print(f"{search_term} not found.")
                return None
    except FileNotFoundError:
        print(f"{file_name} not found")
        
#4. function to make edits to a file
def edit_in_file(file_name, old_term, new_term):
    if not old_term.strip():
        print("INVALID INPUT ❎\nVALUE cannot be blank.")
        return
    if not new_term.strip():
        print("INVALID INPUT ❎\nVALUE cannot be blank.")
        return
    old_term_found = False
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        with open(file_name, "w") as f:
            for line in lines:
                if old_term.lower() in line.lower():  
                    edit_date = time.strftime("%d-%m-%Y %I:%M:%p") 
                    f.write(f"{new_term}| edited on {edit_date}\n")
                    print(f"{old_term} updated to {new_term}.")
                    old_term_found = True
                else:
                    f.write(line)
        if not old_term_found:
            print(f"{old_term} not found in {file_name}")
    except FileNotFoundError:
        print(f"{file_name} not found")
        
#5. function to remove a file
def remove_from_file(file_name, search_term):
    if not search_term.strip():  
        print("VALUE must be provided.")
        return
    search_term_found = False
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        with open(file_name, "w") as f:
            timestamp = time.strftime("%d-%m-%Y %I:%M:%p")
            for line in lines:
                if search_term.lower() in line.lower():
                    print(f"{search_term} removed on {timestamp}.")
                    search_term_found = True
                else:
                    f.write(line)
    except FileNotFoundError:
        print (f"{file_name} not found")
    if not search_term_found:
        print(f"{search_term} record not found.")
        
#6. Function to go back after operation
def go_back():
    while True: 
        go_back = input("Do you want to go back (Y/N):").lower() 
        if go_back not in ["y", "n"]: 
            invalid_input() 
            continue 
        else: 
            return go_back 

#7. Function for invalid input
def invalid_input():
    print("".ljust(18, "*")) 
    print("invalid input ❎".upper()) 

#8.  Function to check if member exists in members.txt file
def check_member_existence(user_name):
    try:
        with open("members.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if user_name.lower() in line.lower():
                    return True
        return False
    except FileNotFoundError:
        print("Member file not found.")
        return False
    
# Function to handle admin login
def admin_login():
    print("Admin Login")
    attempts = 3  #Limit to 3 Attempts

    while attempts > 0: #Loops as long as you have attempts
        username = input("Enter admin username: ") 
        password = input("Enter admin password: ")

        if username in admins and admins[username] == password: #1. Validation for Admin Username/Password #2.Admin/Pass in global scope #
            print(f"Login successful...\nWelcome, {username}!") #User input the right password
            return True  #Breaks loop
        else:
            attempts -= 1 #Reduce attempt in each iteration
            print(f"\nInvalid username or password ❎\nYou have {attempts} attempt(s) left.\n") #Prints feedback with no of attempts left

    print("Too many failed attempts\nExiting admin login...")
    return False  

# Function to handle librarian login
def librarian_login():
    librarianUsername = input("Enter librarian username: ")

    try:
        with open("librarians.txt", "r") as f:
            for line in f:
                username = line.strip().split("|")[0]    
                if librarianUsername.lower() == username.lower(): 
                    print("Username found")
                    return True 
    except FileNotFoundError:
        print("Librarian file not found.")

    print("\nInvalid USERNAME ❎\nPlease try again")
    return False

def checkLibrarypass():
    librarianPassword = input("Enter Password: ")
    if librarianPassword == str(library_pass):
        print("Login successful. Accessing Librarian Menu...")
        return True
    else:
        print("\nInvalid PASSWORD ❎\nPlease try again")
        return False





# Function to add loaned books
def AddLoanedBook(file_name, memberName, bookName, bookFile):
    
    if not check_member_existence(memberName):
        print(f"Error: Member '{memberName}' does not exist.")
        return
    
    try:
   
        with open(bookFile, "r") as books:
            lines = books.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{bookFile}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the book file: {e}")
        return

    bookFound = False
    updatedLines = []
    
    for line in lines:
        if bookName in line:
            bookFound = True
            
            parts = line.split('|')
            try:
                amountAvailablestr = parts[1].strip().split()[-1]  
                amountAvailable = int(amountAvailablestr) 
            except ValueError:
                print(f"Error: The available amount for '{bookName}' is not a valid number.")
                return
            if amountAvailable > 0:

                amountAvailable -= 1
                parts[1] = f"amount available {amountAvailable}"

                
                updatedLine = '|'.join(parts)
                updatedLines.append(updatedLine)
            else:
                print(f"Sorry, the book '{bookName}' is not available for loan (out of stock).")
                return
        else:
            updatedLines.append(line)
    
    if not bookFound:
        print(f"Sorry, the book '{bookName}' is not available in the library.")
        return  


    try:
        with open(bookFile, "w") as books:
            books.writelines(updatedLines)
    except Exception as e:
        print(f"An error occurred while updating the book file: {e}")
        return
    
    # Loan the book if available
    with open(file_name, "a") as f:
        loanDate = time.strftime("%d-%m-%y %I:%M:%p")
        f.write(f"{memberName}| {bookName}| {loanDate}\n")
    
    print(f"Book '{bookName}' loaned to {memberName} on {loanDate}. The updated available amount is {amountAvailable}.")




# Function to search the books catalogue
def searchCatalogue():
    search_term = input("Enter the name or part of the book title to search: ")
    print(f"\n--- Search Results for '{search_term}' ---")
    search_in_file("books.txt", search_term)


# Function to calculate overdue fee
def CalculateFee(daysOverdue):
    if daysOverdue == 1:
        return 2.00
    elif daysOverdue == 2:
        return 3.00
    elif daysOverdue == 3:
        return 4.00
    elif daysOverdue == 4:
        return 5.00
    elif daysOverdue == 5:
        return 6.00
    elif daysOverdue > 5:
        return 10.00
    else:
        return 0.00


# Function to check overdue books from the 'loans.txt' file
def CheckOverdueBooks(file_name):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()

            if not lines:
                print("No loaned books found.")
                return

            print("\n--- Checking for Overdue Books ---")
            for line in lines:
           
                parts = line.strip().split("|")  

    
                if len(parts) != 3:
                    print(f"Skipping invalid entry: {line.strip()}")
                    continue 
                
                memberName, bookName, loanDatestr = [part.strip() for part in parts] 

            
                try:
                    loanDate = datetime.strptime(loanDatestr, "%d-%m-%y %I:%M:%p") 
                except ValueError:
                    print(f"Error parsing date: {loanDatestr} for entry: {line.strip()}")
                    continue  

                currentDate = datetime.now()

               
                daysLoaned = (currentDate - loanDate).days

                if daysLoaned > 14:  # Assuming a 14-day loan period
                    daysOverdue = daysLoaned - 14
                    fee = CalculateFee(daysOverdue)
                    print(f"Book: {bookName} | Borrower: {memberName} | Days Overdue: {daysOverdue} | Fee: RM {fee:.2f}")
                else:
                    print(f"Book: {bookName} | Borrower: {memberName} | Loaned for {daysLoaned} days. Not overdue.")

    except FileNotFoundError:
        print(f"No loan records found in {file_name}.")
def performBookloan():
    memberName = input("Enter member name: ")
    bookName = input("Enter the name of the book: ")

    # Check if the member exists
    if not check_member_existence(memberName):
        print("Member not found.")
        return

    # Check if the member has overdue books
    overdue_books = checkOverdueBooksForMember(memberName)
    if overdue_books:
        print("You have overdue books. Please return them before loaning a new book.")
        for book, daysOverdue in overdue_books:
            fee = CalculateFee(daysOverdue)
            print(f"Overdue Book: {book} | Days Overdue: {daysOverdue} | Fee: RM {fee:.2f}")
        return

    # Check if the member has already loaned 5 books
    if countLoanedBooks(memberName) >= 5:
        print("Loan limit reached. Please return some books before loaning a new one.")
        return

    # Loan the book and record it in loans.txt
    AddLoanedBook("loans.txt", memberName, bookName, "books.txt")
        
def checkOverdueBooksForMember(memberName):
    overdue_books = []
    try:
        with open("loans.txt", "r") as f:
            lines = f.readlines()
            currentDate = datetime.now()

            for line in lines:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    loanMember, bookName, loanDateStr = parts
                    if loanMember.lower() == memberName.lower():
                        loanDate = datetime.strptime(loanDateStr.strip(), "%d-%m-%y %I:%M:%p")
                        daysLoaned = (currentDate - loanDate).days
                        if daysLoaned > 14:  # Assuming a 14-day loan period
                            overdue_books.append((bookName, daysLoaned - 14))
    except FileNotFoundError:
        print("Loan file not found.")
    return overdue_books        
# Function to view loaned books
def viewLoanedBbooks(memberName):
    print(f"\n--- Loaned Books for {memberName} ---")
    try:
        with open("loans.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No loaned books found.")
            else:
                found = False

                for line in lines:
                  
                    parts = line.strip().split("|")
                 
                    if len(parts) == 3:
                        loanMember, bookName, loanDate = parts
                        if loanMember.lower() == memberName.lower():
                            print(f"Book: {bookName} | Loaned on: {loanDate}")
                            found = True

                if not found:
                    print(f"No books loaned by {memberName}.")
    except FileNotFoundError:
        print("No loaned books recorded yet.")
        
# Function to count the books currently loaned by the member
def countLoanedBooks(memberName):
    count = 0
    try:
        with open("loans.txt", "r") as f:
            for line in f:
                loanMember, *_ = line.strip().split("|")
                if loanMember.lower() == memberName.lower():
                    count += 1
    except FileNotFoundError:
        pass
    return count


    
    
def updateMember():
    oldUsername = input("Enter member username to update: ")
    newUsername = input("Enter new username (leave blank to keep current): ")
    newEmail = input("Enter new email (leave blank to keep current): ")
    newPhoneNumber = input("Enter new phone number (leave blank to keep current): ")

    updated = False

    # Read existing members
    try:
        with open("members.txt", "r") as f:
            lines = f.readlines()

        with open("members.txt", "w") as f:
            for line in lines:
                if oldUsername.lower() in line.lower():
                  
                    parts = line.strip().split("|") 
                    if newUsername.strip():
                        parts[0] = newUsername
                    if newEmail.strip():
                        parts[1] = newEmail  
                    if newPhoneNumber.strip():
                        parts[2] = newPhoneNumber 

                   
                    f.write("|".join(parts) + "\n")
                    updated = True
                else:
                    f.write(line)  

    except FileNotFoundError:
        print("Member file not found.")

    if updated:
        print(f"{oldUsername} has been updated.")
    else:
        print(f"{oldUsername} not found.")




import sys

# Main Menu Function
def main_menu():
    while True:
        print("".ljust(30, "-"))
        print("Welcome to Brickfield Library".upper())
        print("".ljust(30, "-"))
        print("Main Menu")
        print("1. Admin")
        print("2. Librarian")
        print("3. Library Member")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 1 and admin_login():
                admin_menu()
            elif choice == 2 and librarian_login() and checkLibrarypass():
                librarian_menu()
            elif choice == 3:
                memberName = input("Enter your member username: ")
                if check_member_existence(memberName):
                    member_menu(memberName)
                else:
                    print("Invalid member username. Please try again.")
            elif choice == 0:
                sys.exit("Thank you for using Brickfields Library".upper())
            else:
                invalid_input()
        else:
            invalid_input()

# Admin Menu Function
def admin_menu():
    while True:
        print("------------")
        print("//Admin Panel//")
        print("1. Add Member")
        print("2. View Members")
        print("3. Search Member")
        print("4. Edit Member")
        print("5. Remove Member")
        print("6. Add Librarian")
        print("7. View Librarians")
        print("8. Search Librarian")
        print("9. Edit Librarian")
        print("10. Remove Librarian")
        print("0. Logout")

        adminChoice = input("Enter your choice: ")
        if adminChoice.isdigit():
            adminChoice = int(adminChoice)

            if adminChoice == 1:
                username = input("Enter member username: ")
                email = input("Enter email: ")
                phone_number = input("Enter Phone Number: ")
                add_to_file("members.txt", username, None, email, phone_number)
            elif adminChoice == 2:
                print("\n-----MEMBERS LIST-----\n")
                view_from_file("members.txt")
            elif adminChoice == 3:
                username = input("Enter member username to search: ")
                search_in_file("members.txt", username)
            elif adminChoice == 4:
                username = input("Enter member username to edit: ")
                newUsername = input("Enter new username: ")
                edit_in_file("members.txt", username, newUsername)
            elif adminChoice == 5:
                username = input("Enter member username to remove: ")
                remove_from_file("members.txt", username)
            elif adminChoice == 6:
                username = input("Enter librarian username: ")
                email = input("Enter email: ")
                phone_number = input("Enter phone number: ")
                add_to_file("librarians.txt", username, None, email, phone_number)
            elif adminChoice == 7:
                print("\n-----LIBRARIANS LIST-----\n")
                view_from_file("librarians.txt")
            elif adminChoice == 8:
                username = input("Enter librarian username to search: ")
                search_in_file("librarians.txt", username)
            elif adminChoice == 9:
                username = input("Enter librarian username to edit: ")
                newUsername = input("Enter new username: ")
                edit_in_file("librarians.txt", username, newUsername)
            elif adminChoice == 10:
                username = input("Enter librarian username to remove: ")
                remove_from_file("librarians.txt", username)
            elif adminChoice == 0:
                break
            else:
                invalid_input()
            if go_back() == "y":
                continue
            else:
                sys.exit("Thank you for using Brickfields Library ❤️".upper())

# Librarian Menu Function
def librarian_menu():
    while True:
        print("--------------")
        print("//Librarian Panel//")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Edit Book")
        print("5. Remove Book")
        print("6. Perform Book Loan")
        print("7. Check Overdue Books")
        print("0. Logout")

        librarian_choice = input("Enter your choice: ")
        if librarian_choice.isdigit():
            librarian_choice = int(librarian_choice)

            if librarian_choice == 1:
                book = input("Enter book name: ")
                quantity = input("Enter quantity: ")
                add_to_file("books.txt", book, quantity, None, None)
            elif librarian_choice == 2:
                print('-----BOOKS LIST-----')
                view_from_file("books.txt")
            elif librarian_choice == 3:
                book = input("Enter book name to search: ")
                search_in_file("books.txt", book)
            elif librarian_choice == 4:
                oldBook = input("Enter book name to edit: ")
                newBook = input("Enter new book name: ")
                edit_in_file("books.txt", oldBook, newBook)
            elif librarian_choice == 5:
                book = input("Enter book name to remove: ")
                remove_from_file("books.txt", book)
            elif librarian_choice == 6:
                performBookloan()
            elif librarian_choice == 7:
                print('-----OVERDUE BOOKS LIST-----')
                CheckOverdueBooks("loans.txt")
            elif librarian_choice == 0:
                break
            else:
                invalid_input()
            if go_back() == "y":
                continue
            else:
                sys.exit("Thank you for using Brickfields Library ❤️".upper())

# Member Menu Function
def member_menu(memberName):
    while True:
        print("".ljust(20, "-"))
        print(f"Welcome {memberName}!".upper())
        print("".ljust(20, "-"))
        print("//Library Member Menu//")
        print("1. View Loaned Books")
        print("2. Update Profile")
        print("3. Search Catalogue")
        print("0. Logout")

        memberChoice = input("Enter your choice: ")
        if memberChoice.isdigit():
            memberChoice = int(memberChoice)

            if memberChoice == 1:
                viewLoanedBbooks(memberName)
            elif memberChoice == 2:
                updateMember(memberName)
            elif memberChoice == 3:
                searchCatalogue()
            elif memberChoice == 0:
                break
            else:
                invalid_input()
            if go_back() == "y":
                continue
            else:
                sys.exit("Thank you for using Brickfields Library ❤️".upper())
            

# Entry Point
if __name__ == "__main__":
    main_menu()
