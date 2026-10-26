class Publication:
    def __init__(self, title, author):
            # private properties
            self.__title = title
            self.__author = author

    # public methods
    def get_title(self,title):
        self.__title = title
    def get_author(self,author):
        self.__author = author

    def set_title(self,title):
         self.__title = title
         return self.__title

    def set_author(self,author):
         self.__author = author
         return self.__author

    def display_info(self):
         print(f"Title: {self.__title}")
         print(f"Author: {self.__author}")


class book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title,author)
        #properties
        self.__number_pages = number_pages
    # Public methods
    def get_number_of_pages(self):
        return self.__number_pages
    
    def set_number_of_pages(self,number_pages):
        if number_pages < 0:
            print("Negative values for number of pages is invalid.")
        else:
            self.__number_pages = number_pages
            return self.__number_pages

class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
            #properties
        self.__issue_number = issue_number
    # Public methods
    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self,issue_number):
        self.__issue_number = issue_number
        return self.__issue_number


#object initialization
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#publication object
print("Publication Information: ")
pub1.display_info()

#book object
print("\nBook information: ")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())  

#magazine object
print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())