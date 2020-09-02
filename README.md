# Sales taxes problem
[![Python](https://img.shields.io/badge/python-3.8-informational)](https://docs.python.org/3/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Actions Status](https://github.com/anjelo95/sales-taxes-problem/workflows/Build%20and%20Test/badge.svg)](https://github.com/anjelo95/sales-taxes-problem/actions)

This problem requires some kind of input. You are free to implement any mechanism for feeding input into your solution (for example, using hard coded data within a unit test). You should provide sufficient evidence that your solution is complete by, as a minimum, indicating that it works correctly against the supplied test data.

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Problem](#PROBLEM:-SALES-TAXES)
* [General requirements](#General-requirements)
* [Solution](#solution)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)



### PROBLEM: SALES TAXES

**Basic sales tax** is applicable at a rate of **10%** on all goods, **except** books, food, and medical products that are exempt. **Import duty** is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.

When I purchase items I receive a receipt which lists the name of all the items and their price (including tax), finishing with the total cost of the items, and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.

Write an application that prints out the receipt details for these shopping baskets...

```
INPUT:

Input 1:
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
3 box of imported chocolates at 11.25

OUTPUT

Output 1:
2 book: 24.98
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 42.32

Output 2:
1 imported box of chocolates: 10.50
1 imported bottle of perfume: 54.65
Sales Taxes: 7.65
Total: 65.15

Output 3:
1 imported bottle of perfume: 32.19
1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
3 imported box of chocolates: 35.55
Sales Taxes: 7.90
Total: 98.38
```

### General requirements
- You may use whatever programming language/platform you prefer. Use something that you know well.
- You must release your work with an OSI-approved open source license of your choice.
- You must deliver the sources of your application, with a README that explains how to compile and run it.
- Add the code to your own Github account and send us the link.

**IMPORTANT:**  Implement the requirements focusing on **writing the best code** you can produce.

### Solution
#### Input Analysis
The input basket has the following format:
```
Input [input_number]:
[quantity] [item] at [price] 
[quantity] [item] at [price] 
...

```
The ```[item]``` must be classified into:
- Basic sales taxable or not
- Import duty taxable or not

The ```[price] ``` is referred to the single item even if the ```[quantity]``` 
is greater than one.

#### Output Analysis
The output recipe has the following format:
```
Output [output_number]:
[quantity] [item]: [price] 
[quantity] [item]: [price] 
...
Sales Taxes: [price]
Total: [price]
```
The ```[output_number]``` is the same of ```[input_number]``` it refers to.

The ```[price] ``` is cumulative for the given ```[item]``` 
and rounded up to the nearest 0.05.

#### Class Diagram
The `Item` abstract class abstracts the single item inside a shopping basket.

The `Item`'s state is defined by:
- the quantity
- the name
- the unitary price

The `Item` is in charge of:
- computing the tax to pay

To make the `Item` resilient to tax rate changes and flexible to new taxes,
the tax computation is delegated to the `TaxCalculator` abstract class.

The `TaxCalculator` abstract class is in charge of:
- classifying the item
- computing the tax for that item

The `Basket` is a concrete class since it already uses only abstractions.
It represents the shopping basket.

The `Basket`'s state is defined by:
- the basket number
- the list of items

The `Basket` is in charge of:
- computing the total price for all the basket's items
- computing the total taxes for all the basket's items
- representing the Basket following the exercise recipe output

The `Receipt` is an abstract class that is in charge of:
- computing the receipt's details given the text representation of the shopping `Baskets`.

The `Receipt` implements the factory design pattern with the abstract method: `create_basket`.
In this way if we need to parse another format of baskets, we just need to implement that method.
The `Receipt` exposes also the protected property `_basket_strings` so that the concrete
class can eventually override how the basket strings can be split from the input text.

The `ExerciseReceipt` is the concrete implementation of the `Receipt`.

The `ExerciseItem` is the concrete implementation of the`Item` under the exercise taxation system.

The `ExerciseTaxCalculator` is the concrete implementation of the `TaxCalculator`
under the exercise taxation system.

To compute the correct tax for a given `ExerciseItem`, `ExerciseTaxCalculator` uses
a simple approach based on a known vocabulary of strings.
To handle this classification problem more rigorously, it could be used a greater 
dictionary stored on secondary storage or use some Machine Learning API.

This means the computation of the correct tax could potentially require
a significant latency due to IO access or network latency.

This is the reason why the methods to get the correct tax (`_is_basic_taxable`, `_is_import_taxable`)
are `cached` trough the usage of the `lru_cache` decorator.


### Installation
First install and configure `poetry` run 
```shell script
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
poetry config virtualenvs.in-project true
```

The clone the repository:
```shell script
git clone git@github.com:anjelo95/sales-taxes-problem.git
```
and change directory:
```shell script
cd sales-taxes-problem
```
 
Then, install dependencies:
```shell script
poetry install
```

### Usage
Once you are in the folder: ```sales-taxes-problem/```:

- run verbose tests with code coverage:
```shell script
poetry run pytest -v --cov='sales_taxes_problem/'
```

- run main entry point:
```shell script
poetry run python sales_taxes_problem/main.py
```
By default the main entry point produces the Receipt details for the exercise shopping Baskets.

You can create your own file with the shopping Baskets (e.g `my_baskets.txt`) and get the Receipt details:
```shell script
echo "Input 1:\n2 book at 12.23">my_baskets.txt

poetry run python sales_taxes_problem/main.py -b my_baskets.txt
```


### Contributing
To contribute, please open a PR based on the `staging` branch, make sure that the new code is properly tested 
and all the steps performed in the CI pipeline are completed successfully. 

We follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/).
