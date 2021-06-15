import unittest
import sort


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        list = [4, 6, 34, 6, 1122, 3, 56, 77879, 65]

        expected = sorted(list)
        sorted_list = sort.bubble_sort(list)

        self.assertEqual(sorted_list, expected)

    def test_select_sort(self):
        list = [4, 6, 34, 6, 1122, 3, 56, 77879, 65]

        expected = sorted(list)
        sorted_list = sort.select_sort(list)

        self.assertEqual(sorted_list, expected)

    def test_insert_sort(self):
        list = [4, 6, 34, 6, 1122, 3, 56, 77879, 65]

        expected = sorted(list)
        sorted_list = sort.insert_sort(list)

        self.assertEqual(sorted_list, expected)

    def test_quick_sort(self):
        list = [4, 6, 34, 6, 1122, 3, 56, 77879, 65]

        expected = sorted(list)
        sorted_list = sort.quick_sort(list)

        self.assertEqual(sorted_list, expected)


if __name__ == "__main__":
    unittest.main()
