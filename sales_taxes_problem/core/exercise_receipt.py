import re
from typing import NamedTuple, Tuple

from sales_taxes_problem.common.basket import Basket
from sales_taxes_problem.common.receipt import Receipt
from sales_taxes_problem.core import ExerciseItem, MalformedBasketError


class ItemArguments(NamedTuple):
    """
    The Item arguments.
    """

    quantity: int
    name: str
    price: float


class BasketInfo(NamedTuple):
    """
    The Basket arguments.
    """

    header: str
    items: Tuple[str, ...]


class ExerciseReceipt(Receipt):
    _ITEM_QUANTITY = r"([0-9]+)"
    _ITEM_NAME = r"(.+)"
    _ITEM_PRICE = r"(\d+.\d\d)"
    _INPUT = r"Input ([0-9]+):"

    # the regex to get the input parameters for the ExerciseItem
    _ITEM_REGEX = re.compile(f"^{_ITEM_QUANTITY} {_ITEM_NAME} at {_ITEM_PRICE}$")

    # the regex to get the Basket number
    _INPUT_REGEX = re.compile(f"^{_INPUT}$")

    def create_basket(self, basket_string: str) -> Basket:

        basket_info = ExerciseReceipt._get_basket_info(basket_string=basket_string)
        basket_header = basket_info.header
        basket_number = ExerciseReceipt._get_basket_number(basket_header=basket_header)
        basket = Basket(number=basket_number)
        for string_item in basket_info.items:
            item_arguments = ExerciseReceipt._get_item_arguments(string_item=string_item)
            item = ExerciseItem(
                quantity=item_arguments.quantity,
                name=item_arguments.name,
                price=item_arguments.price,
            )
            basket.add_item(item)
        return basket

    @staticmethod
    def _get_basket_info(basket_string: str) -> BasketInfo:
        all_lines = basket_string.split("\n")
        non_empty_lines = tuple(filter(lambda line: len(line) > 0, all_lines,))
        if len(non_empty_lines) < 2:
            raise MalformedBasketError(
                f"the basket_string: {basket_string} must contain at least one item"
            )
        return BasketInfo(non_empty_lines[0], non_empty_lines[1:])

    @staticmethod
    def _get_basket_number(basket_header: str) -> int:
        input_match = ExerciseReceipt._INPUT_REGEX.findall(basket_header)
        if input_match is None or len(input_match) == 0:
            raise MalformedBasketError(
                f"the basket_header: {basket_header} must be: `Input [basket_number]:`"
            )

        return int(input_match[0])

    @staticmethod
    def _get_item_arguments(string_item: str) -> ItemArguments:
        try:
            quantity, name, price = ExerciseReceipt._ITEM_REGEX.findall(string_item)[0]
        except (IndexError, TypeError) as ie:
            raise MalformedBasketError(
                f"the string_item: {string_item} must be: `[quantity] [name] at [price]`"
            ) from ie
        if float(price) < 0:
            raise MalformedBasketError(f"the string_item: {string_item} must have a positive price")

        name = ExerciseReceipt._format_item_name(name=name)
        return ItemArguments(quantity=int(quantity), name=name, price=float(price))

    @staticmethod
    def _format_item_name(name: str) -> str:
        if "imported" in name:
            name_without_imported = name.replace("imported ", "")
            return f"imported {name_without_imported}"
        return name
