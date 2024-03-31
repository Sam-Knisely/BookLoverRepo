import pandas as pd
class BookLover():
    """This class has 5 attributes:
        name: The name of the person (type:string)
        email: The person’s email, serving as a unique identifier (type:string)
        fav_genre: The person’s favorite book genre (e.g., mystery, fantasy, or historical fiction).  (type:string)
        num_books: Keeps track of the number of books the person has read (type:int)
        book_list: A dataframe with the columns ['book_name', 'book_rating']
        
        And 4 methods:
        add_book(book_name, rating): This function takes a book name (string) and rating (integer from 0 to 5) and tries to
                                     add the book to book_list if the book is not already in book_list.
        has_read(book_name): This function takes book_name (string) as input and determines if the person has read the book
        num_books_read(): This function takes no parameters and just returns the total number of books the person has read.
        fav_books(): This function takes no parameters and returns the filtered dataframe of the person’s most 
                     favorite books (rating > 3)
        """
    
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
                self.name = name
                self.email = email
                self.fav_genre = fav_genre
                self.num_books = num_books
                self.book_list = book_list
                
    def add_book(self, book_name, rating):
        if book_name not in self.book_list['book_name'].astype(str).values:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
        else:
            print("The book already exists in the book list!")
            
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].astype(str).values:
            return True
        else:
            return False
        
    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]