import unittest
from sorting.bubble_sort import bubble_sort
from sorting.quick_sort import quick_sort, quick_sort_v2
from sorting.selection_sort import selection_sort
from sorting.shell_sort import shell_sort, shell_sort_v2
from sorting.heap_sort import heap_sort
from sorting.merge_sort import merge_sort
from sorting.insertion_sort import insertion_sort
from sorting.bucket_sort import bucket_sort


class TestSort(unittest.TestCase):
    def _test_sort(self, sorting_func, input_list):
        expected_list = sorted(input_list)
        self.assertEqual(sorting_func(input_list), expected_list)

    def _test_sort_all_funcs(self, input_list):
        self._test_sort(bubble_sort, input_list[:])
        self._test_sort(quick_sort, input_list[:])
        self._test_sort(quick_sort_v2, input_list[:])
        self._test_sort(selection_sort, input_list[:])
        self._test_sort(shell_sort, input_list[:])
        self._test_sort(shell_sort_v2, input_list[:])
        self._test_sort(heap_sort, input_list[:])
        self._test_sort(merge_sort, input_list[:])
        self._test_sort(insertion_sort, input_list[:])
        self._test_sort(bucket_sort, input_list[:])

    def test_sort_with_positive_numbers(self):
        input_list = [5, 5, 7, 8, 2, 4, 1]
        self._test_sort_all_funcs(input_list)
        input_list = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
        self._test_sort_all_funcs(input_list)
        input_list = [1, 4, 2, 3.6, -1, 0, 25, -34, 8, 9, 1, 0]
        self._test_sort_all_funcs(input_list)

    def test_sort_negative_numbers_only(self):
        input_list = [-1, -3, -5, -7, -9, -5]
        self._test_sort_all_funcs(input_list)

    def test_sort_with_negative_and_positive_numbers(self):
        input_list = [-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]
        self._test_sort_all_funcs(input_list)

    def test_sort_same_numbers(self):
        input_list = [1, 1, 1, 1]
        self._test_sort_all_funcs(input_list)

    def test_sort_empty_list(self):
        input_list = []
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_already_sorted(self):
        input_list = [1, 2, 3, 4]
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_reversed(self):
        input_list = [4, 3, 2, 1]
        self._test_sort_all_funcs(input_list)

    def test_bubble_sort_disorder_with_repetitions(self):
        input_list = [3, 5, 3, 2, 4, 2, 1, 1]
        self._test_sort_all_funcs(input_list)

    def test_one_number(self):
        input_list = [1]
        self._test_sort_all_funcs(input_list)
