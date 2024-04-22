def summarize_nums(*args):
    return sum(args)


def concat(a, b):
    return f"{a}, {b}"
#
#
# def test_summarize_nums():
#     assert summarize_nums(1, 2, 3, 4) == 10
#     assert isinstance(summarize_nums(1, 2, 3, 4), int)
#
#
# def test_concat():
#     assert concat(1, 2) == "13"
#     assert concat("a", "b") == "a, b"
#
# functions = [
#     test_concat,
#     test_summarize_nums
# ]
# result = summarize_nums("str")
# print(result)
# if __name__ == '__main__':
#     for function in functions:
#         try:
#             function()
#             print(f"{function.__name__} - SUCCESS")
#         except AssertionError as error:
#             print(f"{function.__name__} - FAILED: {error.__dict__}")


import unittest
import sqlite3


class TestSummarizeNums(unittest.TestCase):

    def test_summarize_nums_integer(self):
        self.assertEqual(summarize_nums(1, 2, 3, 4), 10)
        self.assertGreater(summarize_nums(1, 2, 3, 4), 9)

    def test_summarize_nums_string(self):
        self.assertNotIsInstance(summarize_nums(1, 2, 3, 4), str, msg="Must be integer")
        self.assertRaises(TypeError, summarize_nums, "1, 2, 3, 4")


class TestProjectDataBase(unittest.TestCase):

    def setUp(self) -> None:
        self.db_connection = sqlite3.connect("shop.sqlite3")

    def tearDown(self) -> None:
        self.db_connection.close()

    def test_nickname(self):
        command = """SELECT nickname FROM profiles_profile WHERE id=7"""
        cursor = self.db_connection.cursor()
        cursor.execute(command)
        result = cursor.fetchone()
        self.assertEqual(result[0], "test")
