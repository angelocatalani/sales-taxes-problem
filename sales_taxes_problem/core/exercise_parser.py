from typing import Tuple

from sales_taxes_problem.common.basket import Basket
from sales_taxes_problem.common.parser import Parser


class ExerciseParser(Parser):
    def deserialize_receipt(self, receipt_text: str) -> Tuple[Basket]:
        raise NotImplementedError()  # pragma: no cover

    def serialize_receipt(self, baskets: Tuple[Basket]) -> str:
        raise NotImplementedError()  # pragma: no cover
