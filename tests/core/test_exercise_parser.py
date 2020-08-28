import pytest

from sales_taxes_problem.core import ExerciseParser
from tests.core.helpers import ReceiptInfo, load_test_receipts


def test_exercise_parser_init() -> None:
    """
    Test the ExerciseParser init.
    """
    assert ExerciseParser() is not None


@pytest.mark.parametrize(
    "receipt_info", load_test_receipts(),
)  # type: ignore[misc]
def test_exercise_parser_output_receipt(receipt_info: ReceiptInfo) -> None:
    """
    Test the baskets are converted to the
    correct receipt output format.
    """

    ex_parser = ExerciseParser()
    assert ex_parser.output_receipt(baskets=receipt_info.baskets) == receipt_info.output_receipt


@pytest.mark.parametrize(
    "receipt_info", load_test_receipts(),
)  # type: ignore[misc]
def test_exercise_parser_parse_receipt(receipt_info: ReceiptInfo) -> None:
    """
    Test the receipt is converted to the correct Baskets.
    """

    ex_parser = ExerciseParser()
    # FIXME: implement ExerciseParser().parse_receipt()
    with pytest.raises(NotImplementedError):
        assert ex_parser.parse_receipt(receipt=receipt_info.receipt) == receipt_info.baskets
