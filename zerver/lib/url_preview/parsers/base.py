from typing import Any, Text
from bs4 import BeautifulSoup


class BaseParser:
    def __init__(self, html_source):
        # type: (Text) -> None
        self._soup = BeautifulSoup(html_source, "lxml")

    def extract_data(self):
        # type: () -> Any
        raise NotImplementedError()
