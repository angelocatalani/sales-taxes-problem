import re
from typing import List, NamedTuple, Tuple

from sales_taxes_problem.common.basket import Basket
from sales_taxes_problem.common.parser import Parser
from sales_taxes_problem.core import ExerciseItem


class ItemArguments(NamedTuple):
    """
    The Item arguments.
    """

    quantity: int
    name: str
    price: float


class ExerciseParser(Parser):
    """
    Parser for the receipt format of this exercise.
    """

    # the regex to get the parameters for the ExerciseItem
    _ITEM_REGEX = re.compile("^(\d+) (.+) at (\d+.\d\d)$")

    def parse_receipt(self, receipt: str) -> Tuple[Basket, ...]:
        basket_strings = receipt.split("\n\n")
        baskets = []
        basket_number = 1
        for basket_string in basket_strings:
            basket_info = basket_string.split("\n")
            relevant_basket_info = ExerciseParser._filter_invalid_string(basket_info)
            basket = ExerciseParser._build_basket_from_string_items(
                basket_number=basket_number, string_items=relevant_basket_info
            )
            baskets.append(basket)
            basket_number += 1
        return tuple(baskets)

    def output_receipt(self, baskets: Tuple[Basket, ...]) -> str:
        return "".join(str(b) for b in baskets)

    @staticmethod
    def _filter_invalid_string(strings: List[str]) -> Tuple[str, ...]:
        return tuple(filter(lambda s: len(s.strip()) > 0 and "Input" not in s, strings))

    @staticmethod
    def _build_basket_from_string_items(
        basket_number: int, string_items: Tuple[str, ...]
    ) -> Basket:
        basket = Basket(number=basket_number)
        for string_item in string_items:
            item_arguments = ExerciseParser._get_item_arguments(string_item=string_item)
            item = ExerciseItem(
                quantity=item_arguments.quantity,
                name=item_arguments.name,
                price=item_arguments.price,
            )
            basket.add_item(item)
        return basket

    @staticmethod
    def _get_item_arguments(string_item: str) -> ItemArguments:
        quantity, name, price = ExerciseParser._ITEM_REGEX.findall(string_item)[0]
        name = ExerciseParser._format_item_name(name=name)
        return ItemArguments(quantity=int(quantity), name=name, price=float(price))

    @staticmethod
    def _format_item_name(name: str) -> str:
        if "imported" in name:
            name_without_imported = name.replace("imported ", "")
            return f"imported {name_without_imported}"
        return name
