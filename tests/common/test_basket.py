from typing import List
from unittest.mock import MagicMock

import pytest

from sales_taxes_problem.common.basket import Basket
from tests.common.helpers import (
    BASKET_NUMBER,
    EXPECTED_BASKET_FORMAT,
    ITEM_STRING_REPRESENTATION,
    ITEM_TAXED_PRICE,
    ITEM_TAXES,
    ItemTaxInfo,
)


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
    Test the total taxes are correctly computed.
    """
    basket = Basket(number=BASKET_NUMBER)
    for item_info in items_info:
        mocked_item = MagicMock()
        mocked_item.get_taxes = MagicMock(return_value=item_info.taxes * item_info.quantity)
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
    Test the final price is correctly computed.
    """
    basket = Basket(number=BASKET_NUMBER)
    for item_info in items_info:
        mocked_item = MagicMock()
        mocked_item.taxed_price = item_info.taxes * item_info.quantity + item_info.quantity * item_info.price  # type: ignore
        basket.add_item(item=mocked_item)

    assert basket.get_final_price() == final_price


def test_basket_representation() -> None:
    """
    Test the Basket is correctly formatted.
    """
    basket = Basket(number=BASKET_NUMBER)

    mocked_item = MagicMock()
    mocked_item.taxed_price = ITEM_TAXED_PRICE
    mocked_item.get_taxes = MagicMock(return_value=ITEM_TAXES)
    mocked_item.__str__ = MagicMock(return_value=ITEM_STRING_REPRESENTATION)
    basket.add_item(item=mocked_item)

    assert f"{basket}" == EXPECTED_BASKET_FORMAT
