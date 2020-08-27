from abc import ABC, abstractmethod
from typing import Tuple

from sales_taxes_problem.common.basket import Basket


class Parser(ABC):
    @abstractmethod
    def deserialize_receipt(self, receipt_text: str) -> Tuple[Basket]:
        """
        Deserialize the text representing the receipt details into a tuple of Baskets.
        """
        raise NotImplementedError()  # pragma: no cover

    @abstractmethod
    def serialize_receipt(self, baskets: Tuple[Basket]) -> str:
        """
        Serialize the tuple of Baskets into the expected output.
        :param baskets: the tuple of Baskets
        :return: the receipt's output
        """
        raise NotImplementedError()  # pragma: no cover
