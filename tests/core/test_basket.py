from typing import List, Tuple
from unittest.mock import MagicMock, patch

import pytest

from sales_taxes_problem.core import Basket
from tests.core.helpers import BASKET_NUMBER, ItemTaxInfo


def test_basket_init() -> None:
    """
    Test the Basket constructor.
    """
    basket = Basket(number=BASKET_NUMBER)
    assert basket is not None


@pytest.mark.parametrize(
    "items_info,total_taxes",
    [
        ([ItemTaxInfo(taxes=12, quantity=2)], 24.0),
        ([ItemTaxInfo(taxes=12, quantity=2), ItemTaxInfo(taxes=12.35, quantity=1)], 36.35),
        ([ItemTaxInfo(taxes=12, quantity=2), ItemTaxInfo(taxes=12.35, quantity=0)], 24.0),
        ([ItemTaxInfo(taxes=0.35, quantity=2), ItemTaxInfo(taxes=1.5, quantity=2)], 3.70),
        ([], 0.0),
    ],
)  # type: ignore[misc]
def test_basket_get_total_taxes(items_info: List[ItemTaxInfo], total_taxes: int) -> None:
    """
    Test the taxes are correctly computed.
    """
    basket = Basket(number=BASKET_NUMBER)
    for item_info in items_info:

        mocked_item = MagicMock()
        mocked_item.get_taxes = MagicMock(return_value=item_info.taxes)
        mocked_item.quantity = item_info.quantity
        basket.add_item(item=mocked_item)

    assert basket.get_total_taxes() == total_taxes


@pytest.mark.parametrize(
    "items_info,final_price",
    [
        ([ItemTaxInfo(taxes=12, quantity=2, price=100)], 224.0),
        (
            [
                ItemTaxInfo(taxes=12, quantity=2, price=123.35),
                ItemTaxInfo(taxes=12.35, quantity=1, price=50.75),
            ],
            333.80,
        ),
        ([], 0),
    ],
)  # type: ignore[misc]
def test_basket_get_final_price(items_info: List[ItemTaxInfo], final_price: int) -> None:
    """
    Test the taxes are correctly computed.
    """
    basket = Basket(number=BASKET_NUMBER)
    for item_info in items_info:

        mocked_item = MagicMock()
        mocked_item.get_taxes = MagicMock(return_value=item_info.taxes)
        mocked_item.quantity = item_info.quantity
        mocked_item.price = item_info.price
        basket.add_item(item=mocked_item)

    assert basket.get_final_price() == final_price
