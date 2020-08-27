from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    """
    Computes the taxes under a given taxation system.
    """

    @abstractmethod
    def compute_tax(self, item_name: str, item_price: float) -> float:
        """
        Compute the taxes for the input Item's name and price rounded up to the nearest 0.05.

        :param item_name: the item's name
        :param item_price: the item's price

        :return: the taxes for the item_name
        """

        raise NotImplementedError()  # pragma: no cover


class Item(ABC):
    """
    Represents the single Item inside a shopping basket.
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
    def quantity(self) -> int:
        """
        Read-only getter for the quantity attribute.
        """
        return self._quantity

    @property
    def name(self) -> str:
        """
        Read-only getter for the name attribute.
        """
        return self._name

    @property
    def price(self) -> float:
        """
        Read-only getter for the price attribute.
        """
        return self._price

    @property
    @abstractmethod
    def _tax_calculator(self) -> TaxCalculator:
        """
        The tax calculator to compute the Item's tax.

        :return: the TaxCalculator
        """
        raise NotImplementedError()  # pragma: no cover

    def get_taxes(self) -> float:
        """
        Compute the taxes to pay for this single Item rounded up to the nearest 0.05.
        """

        return self._tax_calculator.compute_tax(item_name=self.name, item_price=self.price)
