#!/usr/bin/env python3
"""
Simple pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """The function return a tuple of size two containing a start index and
           an end index corresponding to the range of indexes to return in a
           list for those particular pagination parameters."""
        return (page * page_size - page_size, page * page_size)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Method that return dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        page1, page_size1 = self.index_range(page, page_size)
        dataset = self.dataset()
        if page < page1 and page_size > page_size1:
            return []
        else:
            return dataset[page1: page_size1]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Methodo that return dictionary pagination """
        dataset = self.dataset()
        data_page = self.get_page(page, page_size)
        all_data = len(dataset)
        page1, page_size1 = self.index_range(page, page_size)
        data = data_page
        data_size = len(data)
        total = math.ceil(all_data / page_size)
        if page > 1:
            prev1 = page - 1
        else:
            prev1 = None
        if page < all_data / page_size:
            next1 = page + 1
        else:
            next1 = None
        pagination = {'page_size': data_size,
                      'page': page,
                      'data': data,
                      'next_page': next1,
                      'prev_page': prev1,
                      'total_pages': total}
        return pagination
