from abc import ABC, abstractmethod

from sales_taxes_problem.common.tax_calculator import TaxCalculator


class Item(ABC):
    """
    The single Item inside a shopping Basket.
    """

    def __init__(self, quantity: int, name: str, price: float):
        """
        Initialize a new Item.

        :param quantity: the quantity
        :param name: the name
        :param price: the unitary price regardless of the quantity
        """

        self._quantity = quantity
        self._name = name
        self._price = price

    @property
    @abstractmethod
    def _tax_calculator(self) -> TaxCalculator:
        """
        The tax calculator to compute the Item's tax.

        :return: the TaxCalculator
        """
        raise NotImplementedError()  # pragma: no cover

    @property
    def taxes(self) -> float:
        """
        The taxes to pay for this Item rounded up to the nearest 0.05.
        The taxes are computes for the entire Item quantity.
        """

        return (
            self._tax_calculator.compute_tax(item_name=self._name, item_price=self._price)
            * self._quantity
        )

    @property
    def taxed_price(self) -> float:
        """
        The taxed price for this Item.
        The taxed price is computed for the entire Item quantity.
        """
        return self.taxes + self._price * self._quantity
