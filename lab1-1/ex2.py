import argparse
import math
import operator
import ast


# parse arguments
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("function", help="Python function to run.")
parser.add_argument("args", nargs='*')

arguments = parser.parse_args()

# getting needed function from the built-in libraries
try:
    func = getattr(math, arguments.function)
except AttributeError:
    try:
        func = getattr(operator, arguments.function)
    except AttributeError:
        print("There is no such a mathematical operation")

# literal_eval casts string elements into integers
nums = [ast.literal_eval(arg) for arg in arguments.args]

# calculating the results and printing them
try:
    result = func(*nums)
    print(result)
except Exception as e:
    print(e)
