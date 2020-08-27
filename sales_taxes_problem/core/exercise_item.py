from decimal import Decimal, ROUND_UP

from sales_taxes_problem.common.item import Item, TaxCalculator


class ExerciseTaxCalculator(TaxCalculator):
    """
    Represents the tax computation under this exercise taxation system.
    """

    _BASIC_TAX_PERCENTAGE = 10
    _IMPORT_DUTY_PERCENTAGE = 5

    # the items that are exempted from the basic tax
    _BASIC_TAX_FREE_ITEMS = ["bar", "book", "chocolate", "headache", "pills"]

    # the items that are not exempted from the import duty
    _IMPORT_DUTY_ITEMS = ["imported"]

    @staticmethod
    def round_up(amount: float) -> float:
        """
        Round up the input amount to the nearest 0.05.
        Since we round to the nearest 0.05, the cent can be zero
        (if it is less than or equal five) or five (otherwise).
        When we double the amount and round up to the first decimal
        if the amount's cent is greater than five, the double number
        will have the decimal digits increased by one w.r.t the same amount
        with the cent less than or equal five.
        e.g 1.23 -> 2.46 -> 2.5, 1.26 -> 2.52 -> 2.6 .
        Finally when we divided by two if the amount's cent was greater than 5,
        the rounded number will have 0.05 more than if it was less than 5.

        :param amount: the input amount
        :return: the rounded input
        """

        return float((Decimal(amount) * 2).quantize(Decimal(".1"), rounding=ROUND_UP) / 2)

    def _is_basic_taxable(self, item_name: str) -> bool:
        """
        Check if the basic sales tax applies on the input item.
        It applies all goods, except books, food, and medical products

        :param item_name: the item's name
        :return: True if the item is basic taxable
        """
        return not any(el in item_name for el in self._BASIC_TAX_FREE_ITEMS)

    def _is_import_taxable(self, item_name: str) -> bool:
        """
        Check if the import duty applies on the input item.
        It applies on all imported goods.

        :param item_name: the item's name
        :return: True if the item is import taxable
        """
        return any(el in item_name for el in self._IMPORT_DUTY_ITEMS)

    def compute_tax(self, item_name: str, item_price: float) -> float:
        """
        Compute the tax for the input item.
        Under this exercise taxation system it is 10% for basic sales tax
        and 5% for import duty.

        :param item_name: the item's name
        :param item_price: the item's price
        :return: the tax for the item
        """

        taxes = 0.0
        if self._is_basic_taxable(item_name=item_name):
            taxes += ExerciseTaxCalculator.round_up(self._BASIC_TAX_PERCENTAGE * item_price / 100)

        if self._is_import_taxable(item_name=item_name):
            taxes += ExerciseTaxCalculator.round_up(self._IMPORT_DUTY_PERCENTAGE * item_price / 100)

        return taxes


class ExerciseItem(Item):
    """
    Represents the Item under this exercise taxation system.
    """

    _tax_calculator = ExerciseTaxCalculator()
