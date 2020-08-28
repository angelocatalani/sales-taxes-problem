from typing import Tuple

from sales_taxes_problem.common.basket import Basket
from sales_taxes_problem.common.parser import Parser


class ExerciseParser(Parser):
    """
    Parser for the receipt format of this exercise.
    """

    def parse_receipt(self, receipt: str) -> Tuple[Basket]:
        raise NotImplementedError()  # pragma: no cover

    def output_receipt(self, baskets: Tuple[Basket, ...]) -> str:
        raise NotImplementedError()  # pragma: no cover
