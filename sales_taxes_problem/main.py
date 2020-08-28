from sales_taxes_problem.core import ExerciseParser

if __name__ == "__main__":
    receipt = """Input 1:
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

    parser = ExerciseParser()
    baskets = parser.parse_receipt(receipt=receipt)
    print(parser.output_receipt(baskets=baskets))
