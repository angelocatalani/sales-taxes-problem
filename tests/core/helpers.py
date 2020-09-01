import json
from importlib import resources
from typing import Any, NamedTuple, Tuple

import tests.core.data

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

    baskets: str
    output_receipt: str


def load_data(file: str) -> Any:
    with resources.open_text(tests.core.data, file) as json_file:
        return json.load(json_file)


def load_correct_baskets() -> Tuple[ReceiptInfo, ...]:
    """
    Load the correct baskets.
    """

    test_data = []
    data = load_data("correct_baskets.json")
    for receipt in data:
        ri = ReceiptInfo(baskets=receipt["input"], output_receipt=receipt["output"])
        test_data.append(ri)
    return tuple(test_data)


def load_malformed_baskets() -> Tuple[str, ...]:
    """
    Load the  malformed baskets.
    """

    test_data = []
    data = load_data("malformed_baskets.json")
    for receipt in data:
        test_data.append(receipt["input"])
    return tuple(test_data)
