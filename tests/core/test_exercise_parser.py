import pytest

from sales_taxes_problem.core import ExerciseParser, MalformedReceiptError
from tests.core.helpers import ReceiptInfo, load_correct_receipts, load_malformed_receipts


def test_exercise_parser_init() -> None:
    """
    Test the ExerciseParser init.
    """
    assert ExerciseParser() is not None


@pytest.mark.parametrize(
    "receipt_info", load_correct_receipts(),
)  # type: ignore[misc]
def test_exercise_parser_output_receipt(receipt_info: ReceiptInfo) -> None:
    """
    Test the baskets are converted to the
    correct receipt output format.
    """

    ex_parser = ExerciseParser()
    assert ex_parser.output_receipt(baskets=receipt_info.baskets) == receipt_info.output_receipt


@pytest.mark.parametrize(
    "receipt_info", load_correct_receipts(),
)  # type: ignore[misc]
def test_exercise_parser_parse_receipt(receipt_info: ReceiptInfo) -> None:
    """
    Test the receipt is converted to the correct Baskets.
    """

    ex_parser = ExerciseParser()
    actual_baskets = ex_parser.parse_receipt(receipt=receipt_info.receipt)
    assert len(actual_baskets) == len(receipt_info.baskets)
    for i in range(len(actual_baskets)):
        assert actual_baskets[i] == receipt_info.baskets[i]


@pytest.mark.parametrize(
    "malformed_receipt", load_malformed_receipts(),
)  # type: ignore[misc]
def test_exercise_parser_raise_exception(malformed_receipt: str) -> None:
    """
    Test the receipt is converted to the correct Baskets.
    """

    ex_parser = ExerciseParser()
    with pytest.raises(MalformedReceiptError):
        ex_parser.parse_receipt(receipt=malformed_receipt)
