from typing import List

from sales_taxes_problem.common import Item


class Basket:
    """
    Represents the shopping Basket.
    """

    def __init__(self, number: int):
        """
        Initialize the shopping Basket.

        :param number: the basket number
        """
        self._items: List[Item] = []
        self._number = number

    def add_item(self, item: Item) -> None:
        """
        Add a new Item to this Basket.

        :param item: the Item to add
        """
        self._items.append(item)

    def get_total_taxes(self) -> float:
        """
        Get the taxes to pay for this Basket.

        :return: the taxes to pay
        """
        total_taxes = 0.0
        for item in self._items:
            total_taxes += item.get_taxes() * item.quantity
        return total_taxes

    def get_final_price(self) -> float:
        """
        Get the final price for this Basket.

        :return: the final price
        """
        non_taxed_price = 0.0
        for item in self._items:
            non_taxed_price += item.price * item.quantity
        return self.get_total_taxes() + non_taxed_price
