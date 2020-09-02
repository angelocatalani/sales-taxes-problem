"""
This is the main entry point for the Sales Taxes Problem
"""
import argparse

from sales_taxes_problem.core import ExerciseReceipt

DEFAULT_BASKETS = """Input 1:
2 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85

Input 2:
1 imported box of chocolates at 10.00
1 imported bottle of perfume at 47.50

Input 3:
1 imported bottle of perfume at 27.99
1 bottle of perfume at 18.99
1 packet of headache pills at 9.75
3 box of imported chocolates at 11.25"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-b",
        "--baskets",
        help="the filename containing the shopping baskets",
        type=str,
        required=False,
    )
    args = parser.parse_args()
    baskets_file = args.baskets
    if baskets_file is None:
        receipt = ExerciseReceipt(baskets=DEFAULT_BASKETS)
        print(receipt.details)
    else:
        with open(baskets_file, "r") as file:
            baskets = file.read()
            receipt = ExerciseReceipt(baskets=baskets)
            print(receipt.details)
