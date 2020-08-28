from sales_taxes_problem.common.item import Item
from sales_taxes_problem.core.exercise_tax_calculator import ExerciseTaxCalculator

class ExerciseItem(Item):
    """
    Represents the Item under this exercise taxation system.
    """

    _tax_calculator = ExerciseTaxCalculator()

    def __str__(self) -> str:
        return f"{self._quantity} {self._name}: {self.taxed_price:.2f}"
