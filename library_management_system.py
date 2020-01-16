class Library:

    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Books present in library:{self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender - book database has been updated, you can have book")

        else:
            print(f"Book is already being used by{self.lendDict[book]}")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.booksList.remove(book)


if __name__ == '__main__':

    ashok = Library(["Python", "Rich Daddy Poor Daddy", "C++", "Ruby", "Pearl"], "Ashok")

    while (True):
        print("Welcome to the {ashok.name} library. Enter your choice from below")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = int(input())

        if user_choice == 1:
            ashok.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of book you want to lend")
            user = input("Enter the your name")
            ashok.lendBook(user, book)


        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            ashok.addBook(book)



        elif user_choice == 4:
            book = input("Enter the name of the book you want to return")
            ashok.returnBook(book)
            print("Book is updated")


        else:
            print("Not a valid option")

        print("Press q to Quit and c to Continue")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 == input()
            if user_choice2 == "q":
                print("Thank you for using library")
                quit()

            #             print("Thank you for using library")

            elif user_choice2 == "c":
                continue