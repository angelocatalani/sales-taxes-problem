from abc import ABC, abstractmethod
from typing import Tuple

from sales_taxes_problem.common.basket import Basket


class Parser(ABC):
    """
    Abstract Parser for the receipt.
    """

    @abstractmethod
    def parse_receipt(self, receipt: str) -> Tuple[Basket]:
        """
        Parse the input receipt into a tuple of Baskets.

        :param receipt: the receipt's text
        """
        raise NotImplementedError()  # pragma: no cover

    @abstractmethod
    def output_receipt(self, baskets: Tuple[Basket, ...]) -> str:
        """
        Create the output receipt given the tuple of Baskets it contains.

        :param baskets: the tuple of Baskets
        :return: the receipt's output
        """
        raise NotImplementedError()  # pragma: no cover
