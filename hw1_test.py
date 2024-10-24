import data
import hw1
import unittest

from hw1 import rectangle_area


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = ("Aloha")
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(result,expected)

    def test_vowel_count_2(self):
        input = ("Hello")
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(result,expected)
    # Part 2
    def test_short_lists_1(self):
        input = [[2,4,6],[3,6],[4,8,12,16],[5,10]]
        result = hw1.short_lists(input)
        expected = [[3,6],[5,10]]
        self.assertEqual(result,expected)

    def test_short_lists_2(self):
        input = [[],[-4,8],[8,6],[0,0,0,0,0]]
        result = hw1.short_lists(input)
        expected = [[-4,8],[8,6]]
        self.assertEqual(result,expected)

    # Part 3
    def test_acsending_pairs_1(self):
        input = [[],[-4,8],[8,6],[0,0,0,0,0]]
        result = hw1.ascending_pairs(input)
        expected = [[],[-4,8],[6,8],[0,0,0,0,0]]
        self.assertEqual(result,expected)

    def test_acsending_pairs_2(self):
        input = [[2,4,6],[6,3],[4,8,12,16],[10,5]]
        result = hw1.ascending_pairs(input)
        expected = [[2,4,6],[3,6],[4,8,12,16],[5,10]]
        self.assertEqual(result,expected)

    # Part 4
    def test_add_prices_1(self):
        price1 = data.Price(3, 99)
        price2 = data.Price(5, 56)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(9,55)
        self.assertEqual(result,expected)

    def test_add_prices_2(self):
        price1 = data.Price(3, 40)
        price2 = data.Price(2, 56)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(5,96)
        self.assertEqual(result,expected)

    # Part 5
    def test_rectangle_area_1(self):
        point1 = data.Point(0, 7)
        point2 = data.Point(8, 0)
        rectangle1 = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(rectangle1)
        expected = 56.0
        self.assertEqual(result,expected)

    def test_rectangle_area_2(self):
        point1 = data.Point(4, 8)
        point2 = data.Point(9, 5)
        rectangle1 = data.Rectangle(point1, point2)
        result = hw1.rectangle_area(rectangle1)
        expected = 15.0
        self.assertEqual(result,expected)

    # Part 6
    def test_books_by_author_1(self):
        book1 = data.Book(["Alan Walker"], "The Spectre")
        book2 = data.Book(["Adam Sandler", "Jack Black"], "Comedy")
        book3 = data.Book(["Jack Black"], "Bowser")
        result = hw1.books_by_author("Jack", [book1, book2, book3])
        expected = ["Comedy","Bowser"]
        self.assertEqual(result,expected)

    def test_books_by_author_2(self):
        book1 = data.Book(["Todd","Max","Cat"], "Hawaii")
        book2 = data.Book(["John", "Jill"], "Oklahoma")
        book3 = data.Book(["Abraham Linclon"], "1920")
        result = hw1.books_by_author("Todd", [book1, book2, book3])
        expected = ["Hawaii"]
        self.assertEqual(result,expected)

    # Part 7
    def test_circle_bound_1(self):
        rectangle1 = data.Rectangle(data.Point(0, 8), data.Point(6, 0))
        result = hw1.circle_bound(rectangle1)
        expected = data.Circle(data.Point(3,4),5.0)
        self.assertEqual(result,expected)

    def test_circle_bound_2(self):
        rectangle1 = data.Rectangle(data.Point(3, 12), data.Point(9, 2))
        result = hw1.circle_bound(rectangle1)
        expected = data.Circle(data.Point(6,7),5.8309518948453)
        self.assertAlmostEqual(result,expected)
    # Part 8
    def test_below_pay_average_1(self):
        employee1 = data.Employee("Mark", 20)
        employee2 = data.Employee("Bob", 17)
        employee3 = data.Employee("Josh", 18)
        employee4 = data.Employee("Alex", 23)
        result = hw1.below_pay_average([employee1, employee2, employee3, employee4])
        expected = ["Bob","Josh"]
        self.assertEqual(result, expected)

    def test_below_pay_average_2(self):
        employee1 = data.Employee("Mark", 10)
        employee2 = data.Employee("Bob", 31)
        employee3 = data.Employee("Josh", 20)
        employee4 = data.Employee("Alex", 20)
        result = hw1.below_pay_average([employee1, employee2, employee3, employee4])
        expected = ["Mark","Josh","Alex"]
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
