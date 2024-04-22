import unittest
import sqlite3


def summarize_elements(*args):
    return sum(args)


# print(summarize_elements("1, 2, 3, 4, 5, 6, 7, 8, 9, 10"))
#
# assert summarize_elements(1, 2, 3) == 6
# assert isinstance(summarize_elements(1, 2, 3), str)


class TestSummarizeElements(unittest.TestCase):
    def setUp(self):
        self.data = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_summarize_elements(self):
        res = summarize_elements(*self.data)
        self.assertEqual(res, 45)

    def test_summarize_elements_raise_error(self):
        self.assertRaises(TypeError, summarize_elements, "1, 2, 3")


class TestDataBase(unittest.TestCase):
    def setUp(self):
        self.db_connection = sqlite3.connect('shop.sqlite3')

    def tearDown(self):
        self.db_connection.close()

    def test_select_nickname(self):
        command = ("""SELECT nickname FROM profiles_profile WHERE id=7""")
        cursor = self.db_connection.cursor()
        cursor.execute(command)
        result = cursor.fetchone()
        self.assertEqual(result[0], "test")
