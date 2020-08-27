from typing import NamedTuple, Optional, Tuple
from unittest.mock import MagicMock, patch

import pytest

from sales_taxes_problem.core import Basket

BASKET_NUMBER = 1

ITEM_NAME = "my_items"
ITEM_QUANTITY = 1
ITEM_PRICE = 12.23


class ItemTaxInfo(NamedTuple):
    """
    Internal state of the Item for testing the basket.
    """

    quantity: int
    taxes: float
    price: Optional[float] = None


class ItemInfo(NamedTuple):
    """
    Internal state of the Item for testing the ExerciseItem.
    """

    quantity: int
    name: str
    price: float
