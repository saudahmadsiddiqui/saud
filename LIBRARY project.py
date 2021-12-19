class Library:
    def __init__(self,list,name):
        self.booklist = list
        self.name = name
        self.lenddict = {}

    def displaybook(self):
        print(f" wellcome , we have following books in {self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book in self.booklist and  book not in self.lenddict:
            self.lenddict.update({book: user})
            print("yes you can lend this book")
        elif book in self.lenddict:
            print(f"sorry , this book is already being used by {self.lenddict[book]}")
        else:
            print("Book is not available")




    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added to the book list")
    def returnbook(self,user):
        if book in self.lenddict:
            self.lenddict.pop(book)
            print("book has been added to the booklist")
        else:
            print("being very honest this is not our book")




if __name__ == '__main__':
    saud = Library(["dark night", "harry potter", "python","c++"], "code with saud")

    while(True):
        print(f"Welcome to the {saud.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            saud.displaybook()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            saud.lendbook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            saud.addbook(book)
            print("Book has been added to the book list")


        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            saud.returnbook(book)

        else:
            print("Not a valid option")


        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue
