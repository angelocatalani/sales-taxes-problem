import re
from typing import List, NamedTuple, Tuple

from sales_taxes_problem.common.basket import Basket
from sales_taxes_problem.common.parser import Parser
from sales_taxes_problem.core import ExerciseItem, MalformedReceiptError


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
    _ITEM_QUANTITY = r"(\d+)"
    _ITEM_NAME = r"(.+)"
    _ITEM_PRICE = r"(\d+.\d\d)"
    _ITEM_REGEX = re.compile(f"^{_ITEM_QUANTITY} {_ITEM_NAME} at {_ITEM_PRICE}$")

    def parse_receipt(self, receipt: str) -> Tuple[Basket, ...]:
        """
        Parse the input receipt into a tuple of Baskets.

        :param receipt: the receipt's text
        :raise MalformedReceiptError: if the receipt is not well formatted
        """
        basket_strings = ExerciseParser._get_basket_strings(receipt=receipt)

        baskets = []
        basket_number = 1

        for basket_string in basket_strings:
            basket = ExerciseParser._build_basket_from_string(
                basket_number=basket_number, basket_string=basket_string
            )
            baskets.append(basket)
            basket_number += 1
        return tuple(baskets)

    def output_receipt(self, baskets: Tuple[Basket, ...]) -> str:
        return "\n".join(str(b) for b in baskets)

    @staticmethod
    def _get_basket_strings(receipt: str) -> Tuple[str, ...]:

        basket_strings = receipt.split("\n\n")
        for basket_string in basket_strings:
            if not ExerciseParser._is_valid_basket(basket_string):
                raise MalformedReceiptError(
                    f"the basket:{basket_string} is not formatted correctly"
                )
        return tuple(basket_strings)

    @staticmethod
    def _is_valid_basket(basket_string: str) -> bool:
        # FIXME: use regex
        return "Input" in basket_string

    @staticmethod
    def _filter_invalid_baskets_string(strings: List[str]) -> Tuple[str, ...]:
        return tuple(filter(lambda s: len(s.strip()) > 0 and "Input" in s, strings))

    @staticmethod
    def _build_basket_from_string(basket_number: int, basket_string: str) -> Basket:
        basket_info = basket_string.split("\n")
        relevant_basket_info = ExerciseParser._filter_invalid_item_string(basket_info)
        basket = Basket(number=basket_number)
        for string_item in relevant_basket_info:
            try:
                item_arguments = ExerciseParser._get_item_arguments(string_item=string_item)
                item = ExerciseItem(
                    quantity=item_arguments.quantity,
                    name=item_arguments.name,
                    price=item_arguments.price,
                )
                basket.add_item(item)
            except Exception as e:
                raise MalformedReceiptError(
                    f"the string item: {string_item} is not valid `quantity`, `name`, `price` inputs for the ExerciseItem"
                ) from e
        return basket

    @staticmethod
    def _filter_invalid_item_string(strings: List[str]) -> Tuple[str, ...]:
        return tuple(filter(lambda s: len(s.strip()) > 0 and "Input" not in s, strings))

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
