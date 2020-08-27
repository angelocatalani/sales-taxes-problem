from typing import NamedTuple

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
