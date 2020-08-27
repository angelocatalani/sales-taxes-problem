from typing import NamedTuple, Optional, Tuple
from unittest.mock import MagicMock, patch

import pytest

from sales_taxes_problem.core import Basket

BASKET_NUMBER = 1


class ItemInfo(NamedTuple):
    """
    Basic internal state of the Item for testing purposes.
    """

    quantity: int
    taxes: float
    price: Optional[float] = None
