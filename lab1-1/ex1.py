import argparse


# parsing arguments
parser = argparse.ArgumentParser()

parser.add_argument("num1")
parser.add_argument("operation")
parser.add_argument("num2")

args = parser.parse_args()

# calculates result using eval function
try:
    if args.operation not in ["+", "-", "/", "*"]:
        raise Exception("Error, wrong arithmetic operator")
    result = eval(args.num1 + args.operation + args.num2)
    print(round(result, len(str(int(result)))+2))
except Exception as e:
    print(e)
