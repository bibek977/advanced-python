class Library:
    def __init__(self,bookList):
        self.books = bookList

    def displayBooks(self):
        print("The list of books are : ")
        for book in self.books:
            print(book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have borrowed {bookName}")
            self.books.remove(bookName)
            return True
        else:
            print(f"{bookName} is not avaliable this time")
            return False

    def returnedBook(self,bookName):
        self.books.append(bookName)
        print(f"Thanks for returning {bookName}")

class Student:
    def requestBook(self):
        self.book = input("Enter a book name to borrow : ")
        return self.book
    
    def returnBook(self):
        self.book=input("Enter the book name want to return : ")
        return self.book

if __name__== "__main__":
    mainLibrary = Library(["python","react","javascript","scss","css","html","django"])

    student = Student()

    while(True):
        welcome = ''' Welcome to the library Menu  :
        1. display all the book list
        2. request a book
        3. return a book
        4. exit '''

        print(welcome)

        choice = int(input("Enter your choice : "))

        if(choice==1):
            mainLibrary.displayBooks()

        elif(choice==2):
            # bookName=input("Name of Book : ")
            mainLibrary.borrowBook(student.requestBook())

        elif(choice==3):
            # bookName = input("Returning Book name : ")
            mainLibrary.returnedBook(student.returnBook())

        elif(choice==4):
            print("Thank you")
            exit()

        else: 
            print("Enter Valid choice")