from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    """
    Compute the taxes under a given taxation system.
    """

    @abstractmethod
    def compute_tax(self, item_name: str, item_price: float) -> float:
        """
        Compute the taxes for the given item_name and item_price rounded up to the nearest 0.05.

        :param item_name: the item's name
        :param item_price: the item's price

        :return: the taxes for the item_name
        """

        raise NotImplementedError()  # pragma: no cover
