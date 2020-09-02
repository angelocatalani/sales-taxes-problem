from abc import ABC, abstractmethod
from decimal import Decimal, ROUND_UP


class TaxCalculator(ABC):
    """
    The taxation system.
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

    def round_up(self, amount: float) -> float:
        """
        Round up the input amount to the nearest 0.05.
        Since we round to the nearest 0.05, the cent can be zero
        (if it is less than or equal five) or five (otherwise).
        When we double the amount and round up to the first decimal
        if the amount's cent is greater than five, the double number
        will have the decimal digits increased by one w.r.t the same amount
        with the cent less than or equal five.
        e.g 1.23 -> 2.46 -> 2.5, 1.26 -> 2.52 -> 2.6 .
        Finally when we divided by two if the amount's cent was greater than 5,
        the rounded number will have 0.05 more than if it was less than 5.

        :param amount: the amount
        :return: the rounded amount
        """

        return float((Decimal(amount) * 2).quantize(Decimal(".1"), rounding=ROUND_UP) / 2)
