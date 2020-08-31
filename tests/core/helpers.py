import json
from importlib import resources
from typing import Any, Dict, List, NamedTuple, Tuple

import tests.core.data
from sales_taxes_problem.common.basket import Basket
from sales_taxes_problem.core import ExerciseItem

BASKET_NUMBER = 1

ITEM_NAME = "my_item"
ITEM_QUANTITY = 1
ITEM_PRICE = 12.23


class ItemInfo(NamedTuple):
    """
    Internal state of the Item for testing the ExerciseItem.
    """

    quantity: int
    name: str
    price: float


class ReceiptInfo(NamedTuple):
    """
    Auxiliary data structure to test the ExerciseParser.
    """

    receipt: str
    baskets: Tuple[Basket, ...]
    output_receipt: str


def load_correct_receipts() -> Tuple[ReceiptInfo, ...]:
    """
    Load the well formatted receipts.
    """

    def _build_basket_from_items(number: int, item_list: List[Dict[str, Any]]) -> Basket:
        basket = Basket(number=number)
        for item in item_list:
            deserialized_item = ExerciseItem(
                quantity=item["quantity"], name=item["name"], price=item["price"]
            )
            basket.add_item(item=deserialized_item)
        return basket

    test_data = []
    with resources.open_text(tests.core.data, "correct_receipts.json") as json_file:
        data: Any = json.load(json_file)
        for receipt in data:
            basket_counter = 1
            input_receipt = receipt["input"]
            output_receipt = receipt["output"]
            items = receipt["items"]
            baskets = []
            for item_list in items:
                basket = _build_basket_from_items(number=basket_counter, item_list=item_list)
                baskets.append(basket)
                basket_counter += 1
            ri = ReceiptInfo(
                receipt=input_receipt, baskets=tuple(baskets), output_receipt=output_receipt
            )
            test_data.append(ri)

    return tuple(test_data)


def load_malformed_receipts() -> Tuple[str, ...]:
    """
    Load the  malformed receipts.
    """

    test_data = []
    with resources.open_text(tests.core.data, "malformed_receipts.json") as json_file:
        data: Any = json.load(json_file)
        for receipt in data:
            test_data.append(receipt["input"])
    return tuple(test_data)
