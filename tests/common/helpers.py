from typing import NamedTuple, Optional

BASKET_NUMBER = 1


class ItemTaxInfo(NamedTuple):
    """
    Internal state of the Item for testing the basket.
    """

    quantity: int
    taxes: float
    price: Optional[float] = None
