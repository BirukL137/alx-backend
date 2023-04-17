#!/usr/bin/env python3
"""
Hypermedia pagination
"""

import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This function takes two integer arguments page with default
        value 1 and page_size with default value 10.

        Args:
            page (int): an integer type page with default value 1.
            page_size (int): an integer type page_size with default
            value 10.

        Returns:
            empty list if input argument is out of range for the dataset.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        start_index = index_range(page, page_size)[0]
        end_index = index_range(page, page_size)[1]

        try:
            return self.dataset()[start_index:end_index]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        This function returns a dictionary containing the following
        key-value pairs:
          page_size: the length of the returned dataset page
          page: the current page number
          data: the dataset page (equivalent to return from previous task)
          next_page: number of the next page, None if no next page
          prev_page: number of the previous page, None if no previous page
          total_pages: the total number of pages in the dataset as an integer
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        data = self.get_page(page=page, page_size=page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = None if (page + 1) > total_pages else (page + 1)

        prev_page = None if (page - 1) < 1 else (page - 1)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
