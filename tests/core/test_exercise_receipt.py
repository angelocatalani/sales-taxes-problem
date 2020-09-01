import pytest

from sales_taxes_problem.core import ExerciseReceipt
from sales_taxes_problem.core.exceptions import MalformedBasketError
from tests.core.helpers import ReceiptInfo, load_correct_baskets, load_malformed_baskets


def test_exercise_receipt_init() -> None:
    """
    Test the ExerciseReceipt init.
    """
    assert ExerciseReceipt(baskets="") is not None


@pytest.mark.parametrize(
    "receipt_info", load_correct_baskets(),
)  # type: ignore[misc]
def test_exercise_receipt_details(receipt_info: ReceiptInfo) -> None:
    """
    Test the Receipt details are computed correctly.
    """

    ex_receipt = ExerciseReceipt(baskets=receipt_info.baskets)
    assert ex_receipt.details == receipt_info.output_receipt


@pytest.mark.parametrize(
    "malformed_baskets", load_malformed_baskets(),
)  # type: ignore[misc]
def test_exercise_receipt_raise_exception(malformed_baskets: str) -> None:
    """
    Test the MalformedBasketsError is raised when the baskets are malformed.
    """

    ex_receipt = ExerciseReceipt(baskets=malformed_baskets)
    with pytest.raises(MalformedBasketError):
        ex_receipt.details
