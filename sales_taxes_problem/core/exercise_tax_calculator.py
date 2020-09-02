from functools import lru_cache

from sales_taxes_problem.common.tax_calculator import TaxCalculator


class ExerciseTaxCalculator(TaxCalculator):
    _BASIC_TAX_PERCENTAGE = 10
    _IMPORT_DUTY_PERCENTAGE = 5

    # the items that are exempted from the basic tax
    _BASIC_TAX_FREE_ITEMS = ["bar", "book", "chocolate", "headache", "pills"]

    # the items that are not exempted from the import duty
    _IMPORT_DUTY_ITEMS = ["imported"]

    def compute_tax(self, item_name: str, item_price: float) -> float:
        """
        Compute the tax for the given Item.
        Under this exercise taxation system it is 10% for basic sales tax
        and 5% for import duty.

        :param item_name: the Item's name
        :param item_price: the Item's price
        :return: the tax for the Item
        """

        taxes = 0.0
        if self._is_basic_taxable(item_name=item_name):
            taxes += self.round_up(self._BASIC_TAX_PERCENTAGE * item_price / 100)

        if self._is_import_taxable(item_name=item_name):
            taxes += self.round_up(self._IMPORT_DUTY_PERCENTAGE * item_price / 100)

        return taxes

    @lru_cache(maxsize=128)
    def _is_basic_taxable(self, item_name: str) -> bool:
        """
        Check if the basic sales tax applies on the given Item.
        It applies all goods, except books, food, and medical products.

        :param item_name: the Item's name
        :return: True if the Item is basic taxable, False otherwise
        """
        return not any(el in item_name for el in self._BASIC_TAX_FREE_ITEMS)

    @lru_cache(maxsize=128)
    def _is_import_taxable(self, item_name: str) -> bool:
        """
        Check if the import duty applies on the given Item.
        It applies on all imported goods.

        :param item_name: the Item's name
        :return: True if the Item is import taxable, False otherwise
        """
        return any(el in item_name for el in self._IMPORT_DUTY_ITEMS)
