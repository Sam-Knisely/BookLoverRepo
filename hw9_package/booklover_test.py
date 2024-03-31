import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1 = BookLover("Sam", "email1", "scifi", 4)
        test1.add_book("Three Body Problem", 5)
        self.assertTrue("Three Body Problem" in test1.book_list['book_name'].values)
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test2 = BookLover("Sam", "email1", "scifi")
        test2.add_book("Three Body Problem", 5)
        test2.add_book("Three Body Problem", 5)
        value_count = test2.book_list['book_name'].value_counts()
        self.assertEqual(value_count["Three Body Problem"],1)
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        books =   pd.DataFrame({
            'book_name': ["Three Body Problem", "Cook book"],
            'book_rating': [5, 1]
        })
        test3 = BookLover("Sam", "email1", "scifi", 4, books)
        self.assertTrue(test3.has_read("Three Body Problem"))
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        books =   pd.DataFrame({
            'book_name': ["Three Body Problem", "Cook book"],
            'book_rating': [5, 1]
        })
        test4 = BookLover("Sam", "email1", "scifi", 4, books)
        self.assertFalse(test4.has_read("Red Rising"))
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test5 = BookLover("Sam", "email1", "scifi")               
        test5.add_book("Three Body Problem", 5)
        test5.add_book("Cook Book", 1)  
        self.assertEqual(test5.num_books_read(), 2)
        
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test6 = BookLover("Sam", "email1", "scifi")               
        test6.add_book("Three Body Problem", 5)
        test6.add_book("Cook Book", 1)
        test6.add_book("Red Rising", 4)
        fav_books_test = test6.fav_books()
        for i in fav_books_test['book_rating']:
            self.assertTrue(i > 3)

if __name__ == '__main__':
    
    unittest.main(verbosity=3)