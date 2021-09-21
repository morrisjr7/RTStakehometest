'''
Takes in a target integer and prints the values that are above and below the target in an array.
e.g. 'python integerabovebelow.py 6' will return: “above: 1, below: 4”
Also takes optional arguments to pass in a custom array and print the number of elements equal to the target integer.
'''
import argparse

# Initialize variables
default_array = [1, 5, 2, 1, 10]
array_used = []
above = 0
below = 0
equal = 0

# Handle incoming arguments
parser = argparse.ArgumentParser()
parser.add_argument('target_int', type=int)
# The array will be parsed from this string later.
parser.add_argument('--array', type=str)
parser.add_argument('--include_equal', action='store_true')
args = parser.parse_args()
target = args.target_int

# If else to handle optional array input
if args.array:
    # Parse array string using list comprehension
    array_used = [int(x) for x in args.array.split(',')]
else:
    array_used = default_array
# Main loop to count the above,below,equal
for element in array_used:
    if args.target_int > element:
        below += 1
    elif args.target_int == element:
        equal += 1
    else:
        above += 1
# If else to handle optional inclusion of equal values
if args.include_equal:
    print("above:" + str(above) + " below:" + str(below) + " equal:" + str(equal))
else:
    print("above:" + str(above) + " below:" + str(below))
