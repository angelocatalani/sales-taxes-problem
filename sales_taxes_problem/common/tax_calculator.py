from abc import ABC, abstractmethod


class TaxCalculator(ABC):
    """
    Computes the taxes under a given taxation system.
    """

    @abstractmethod
    def compute_tax(self, item_name: str) -> float:
        """
        Compute the taxes for the input Item's name rounded up to the nearest 0.05.

        :return: the taxes for the item_name
        """

        raise NotImplementedError()  # pragma: no cover
