from typing import List

from sales_taxes_problem.common.item import Item


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
            total_taxes += item.get_taxes()
        return total_taxes

    def get_final_price(self) -> float:
        """
        Get the final price for this Basket.

        :return: the final price
        """
        final_price = 0.0
        for item in self._items:
            final_price += item.taxed_price
        return final_price

    def __str__(self) -> str:
        header = f"\nOutput {self._number}:\n"
        items_to_string = "\n".join(str(i) for i in self._items)
        sales_taxes = f"\nSales Taxes: {self.get_total_taxes()}"
        total = f"\nTotal: {self.get_final_price()}\n"

        return f"{header}{items_to_string}{sales_taxes}{total}"
