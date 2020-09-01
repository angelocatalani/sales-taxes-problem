from typing import NamedTuple, Optional

BASKET_NUMBER = 1
ITEM_STRING_REPRESENTATION = "1 music CD: 16.49"
ITEM_TAXED_PRICE = 16.49
ITEM_TAXES = 1.50
EXPECTED_BASKET_FORMAT = f"Output 1:\n{ITEM_STRING_REPRESENTATION}\nSales Taxes: {ITEM_TAXES:.2f}\nTotal: {ITEM_TAXED_PRICE:.2f}\n"


class ItemTaxInfo(NamedTuple):
    """
    Internal state of the Item for testing the basket.
    """

    quantity: int
    taxes: float
    price: Optional[float] = None
