import argparse

parser = argparse.ArgumentParser()
parser.add_argument("formula")
args = parser.parse_args()

isFormula = True

# checks if formula starts and ends in a number
if not (args.formula[0].isdigit() and args.formula[-1].isdigit()):
    isFormula = False

# checks for wrong number of signs
elif args.formula.find("++") != -1 or args.formula.find("--") != -1:
    isFormula = False

# removes all the signs from formula and checks whether it's digit
else:
    check = args.formula.replace("+", "")
    check = check.replace("-", "")
    if not check.isdigit():
        isFormula = False

# if formula is correct, program calculates it and shows the result, otherwise it tells that formula is incorrect
if isFormula:
    result = eval(args.formula)
    print("\nresult = (" + str(isFormula) + ", " + str(result) + ")")
else:
    print("\nresult = (" + str(isFormula) + ", None)")
