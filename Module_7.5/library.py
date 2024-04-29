class Book:
    def __init__(self, accessionNum, name, author, category, quantity) -> None:
        self.accessionNum = accessionNum
        self.name = name
        self.author = author
        self.category = category
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"Accession Number: {self.accessionNum} | Name: '{self.name}' | Author: '{self.author}' | Category: '{self.category} ."


class User:
    def __init__(self, name, id, email, password) -> None:
        self.name = name
        self.id = id
        self.email = email
        self.password = password
        
class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books = []
        self.users = []
        self.borrowedBooksAccessionNum = []
        self.borrowedBooks = []

    def add_book(self, name, author, category,quantity):
        for i in range(quantity):
            accessionNum = len(self.books)+1
            self.books.append(Book(accessionNum, name,author,category,quantity))

        print(f"\n {quantity} piece {name} book addedd successfully!!!")

    def add_user(self, name, id, email, password):
        user = User(name,id,email,password)
        self.users.append(user)
        print("User added successfully!!!")
        return user

    def borrow_book(self,user, accessionNum):

        for book in self.books:
            if book.accessionNum == accessionNum: 
                if book in self.borrowedBooks:
                    print("Already this book has been borrwed") 
                    return
                else:
                    print(f"Here is your {book.name} ")
                    self.borrowedBooks.append(book)
                    return
       
        print("Sorry this book is not available in our library")

    def return_book(self, user, accessionNum):
        for book in self.borrowedBooks:
            if accessionNum == book.accessionNum:
                print(f"The book successfully returned, Thank You !!!")
                self.borrowedBooks.pop(self.borrowedBooks.index(book))
            else:
                print("Sorry your book return is not successfull. Give right info")

    def all_books(self):
        for book in self.books:
            print(book)
            print("-------------------------------------------------------------------------------------------")
    def all_borrowed_books(self):
        for book in self.borrowedBooks:
            print(book)
            print("-------------------------------------------------------------------------------------------")

    def all_users(self):
        for user in self.users:
            print(f"Name: '{user.name} | ID: {user.id} | Email: '{user.email}' .")
            print("-------------------------------------------------------------------------------------------")

aybrary = Library('aybrary')

admin = aybrary.add_user('admin', 100200300, 'admin@aybrary.com', 'admin')
shahid = aybrary.add_user("Shahid Afridi", 191378038, "shahidafridi.cse@gmail.com", "12345")

aybrary.add_book("Django Pro", "Ayman Afridi", "Programming",2)
aybrary.add_book("Introduction to Python", "Jhankar Mahbub", "Programming",5)



run = True
currentUser = admin

while run:
    if currentUser == None:
        print("-------- No Logged in User --------")
        option = input("Login ? Registration ? (L/R): ") 
        
        if option == 'R':
            id = int(input("\tEnter Your 9 Digit ID : "))
            name = input("\tEnter Your Name : ")
            email = input("\tEnter Your Email : ")
            password = input("\tEnter Your Password : ")

            user = aybrary.add_user(name,id,email,password)
            currentUser = user
            

        elif option == 'L':
            email = input("\tEnter Your Email : ")
            password = input("\tEnter Your Password : ")
            
            userFound = False
            for user in aybrary.users:
                if user.email == email and user.password == password:
                    currentUser = user
                    userFound = True
                    break 
            
            if not userFound:
                print("\tSorry !!! User Not Found. Try Again")

    else:
        if currentUser.email == 'admin@aybrary.com':
            print("------------ Hello Admin ------------")
            print("Options: \n")

            print("1: Add Book")
            print("2: Show All Books")
            print("3: Show Borrowed Books")
            print("4: Show Users")
            print("404: Logout")
            print("420: For end the program type 420")

            op = input("\nEnter Option: ")
            
            print("-------------------------------------------------------------------------------------------")

            if op =='1':
                name = input("\tEnter The Book Name : ")
                author = input("\tEnter The Name of Author : ")
                category = input("\tEnter The Category : ")
                quantity = int(input("\tEnter The Quantity : "))

                aybrary.add_book(name,author,category,quantity)
            elif op == '2':
                aybrary.all_books()
            elif op == '3':
                aybrary.all_borrowed_books()

            elif op == '4':
                aybrary.all_users()

            elif op == '404':
                currentUser = None
            elif op == '420':
                break
            else:
                print("!!!!!!!!!!!!  Type Correct Option  !!!!!!!!!!!! \n")

        
        else:
            print(f"------------ Hello {user.name} ------------")

            print("Options: \n")

            print("1: Borrow Book")
            print("2: Return Book")
            print("3: Show My Borrowed Books")
            print("4: Show All Books")

            print("404: Logout")
            print("420: For end the program type 420")

            op = input("\nEnter Option: ")
            print("-------------------------------------------------------------------------------------------")
            

            if op == '1':
                accessionNum = int(input("\tPlease enter the accession number of the book: "))
                aybrary.borrow_book(currentUser,accessionNum)

            elif op == '2':
                accessionNum = input("\tEnter The Acccession Number: ")
                aybrary.return_book(currentUser, accessionNum)
                
            elif op == '3':
                aybrary.all_borrowed_books()

            elif op == '4':
                aybrary.all_books()

            elif op == '404':
                currentUser = None  
            elif op == '420':
                break
            else:
                print("!!!!!!!!!!!!  Type Correct Option  !!!!!!!!!!!! \n")



