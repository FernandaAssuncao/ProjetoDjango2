from utils.pagination import make_pagination_range
from unittest import TestCase


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_ranges(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qyt_paginas=4,
            current_page=1
        )
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):
        ...
