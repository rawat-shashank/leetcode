import unittest
from typing import List

class MyCalendar:

    def __init__(self):
        self.books = []

    def book(self, start: int, end: int) -> bool:
        for x, y in self.books:
            if x < end and start < y:
                return False
        self.books.append((start, end))
        return True

class Tests(unittest.TestCase):
    def tests(self):
        sol = MyCalendar()
        self.assertEqual(True, sol.book(10, 20))
        self.assertEqual(False, sol.book(15, 25))
        self.assertEqual(True, sol.book(20, 30))
        

if __name__ == '__main__':
    unittest.main()