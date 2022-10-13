import argparse


# parsing arguments
parser = argparse.ArgumentParser()
parser.add_argument("capacity", type=int)
parser.add_argument("bars", nargs="*")
args = parser.parse_args()

try:
    goldenBars = [int(item) for item in args.bars]
    length = len(goldenBars)

    # Next part makes a memorization matrix with all combinations of gold weights

    matrix = [[0 for j in range(args.capacity + 1)] for i in range(length + 1)]

    for i in range(length + 1):
        for j in range(args.capacity + 1):
            if not i or not j:
                matrix[i][j] = 0
            elif goldenBars[i - 1] <= j:
                matrix[i][j] = max(goldenBars[i - 1] + matrix[i - 1][j - goldenBars[i - 1]], matrix[i - 1][j])
            else:
                matrix[i][j] = matrix[i - 1][j]

    print("Maximum: ", matrix[length][args.capacity])
except Exception as e:
    print(e)
