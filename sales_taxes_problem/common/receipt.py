from abc import ABC, abstractmethod
from typing import Tuple

from sales_taxes_problem.common.basket import Basket


class Receipt(ABC):
    """
    The collection of shopping Baskets.
    Adopted the Factory design pattern to create Baskets from strings.
    """

    def __init__(self, baskets: str):
        """
        Initialize the Receipt with the string representation of multiple Baskets.

        :param baskets: the string representation of a Basket collection
        """
        self._baskets = baskets

    @property
    def _basket_strings(self) -> Tuple[str, ...]:
        """
        The tuple of Basket strings inside the Receipt.
        """
        return tuple(self._baskets.split("\n\n"))

    @property
    def details(self) -> str:
        """
        Compute the Receipt details for the given shopping Baskets.

        :return: the Receipt details
        """
        baskets = []
        for basket_string in self._basket_strings:
            basket = self.create_basket(basket_string=basket_string)
            baskets.append(basket)
        return "\n".join(str(b) for b in baskets)

    @abstractmethod
    def create_basket(self, basket_string: str) -> Basket:
        """
        Create the Basket from the Basket string representation.

        :param basket_string: the text representing the Basket
        :return: the Basket instance
        """
        raise NotImplementedError()  # pragma: no cover
